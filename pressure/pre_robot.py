#! /usr/bin/env
#coding=utf-8

from robot import SpinRobot
import gen.proto as pb
from net import *
from controller import *


class PreRobot(SpinRobot):
    def __init__(self, addr, name, theme_id, life):
        SpinRobot.__init__(self, name, theme_id)
        self.life = int(life)
        self.set_auto_interval(0.001)
        self.log_switch = False
        self.transportor = Transportor(addr)
        self.controller = create_theme_controller(theme_id)

    def print_user_data(self):
        self.log("[name:%s uid:%d token:%s life:%d]" % (self.name, self.player_id, self.token, self.life))

    def send_packet(self, req):
        if self.err_count >= self.err_max:
            self.log_err("err max")
            exit(1)

        rsp = self.transportor.send_result(req)
        self.on_response(rsp)

    def req_debug(self, player_id, theme_id, cmd, bet):
        self.log("req_debug : ", cmd)
        req = make_debug_req(player_id, theme_id, cmd, bet)
        self.transportor.send_debug(req)

    def req_debug_cmd(self, player_id, theme_id, cmd, bet):
        self.log("req_debug : ", cmd)
        req = make_debug_cmd_req(player_id, theme_id, cmd, bet)
        self.transportor.send_debug(req)

    def send_gm(self, cmd):
        self.req_debug(self.player_id, self.theme_id, cmd, self.themeData.get_play_bet())

    def send_cmd(self, cmd):
        self.req_debug_cmd(self.player_id, self.theme_id, cmd, self.themeData.get_play_bet())

    # response
    def on_login(self, packet):
        login = packet.Login
        self.set_user_data(login.PlayerID, login.Token)
        self.print_user_data()     

    def on_response(self, packet):
        if packet.Error != None and len(packet.Error.Msg) > 0:
            self.process_err(packet.Error)
            self.err_count += 1
            self.log_err("[code:%d] [mgs:%s]err_count:%d" % (packet.Error.Code, packet.Error.Msg, self.err_count))
            return

        if packet.HasField("Login"):
            self.on_login(packet)
            return

        for r in packet.Multi.Responses:
            if r.HasField("ThemeStatus"):
                self.on_theme_status(r.ThemeStatus)
            elif r.HasField("Play"):
                self.on_play(r.Play)
                pass
        
    def on_play(self, packet):
        self.themeData.update_from_play(packet)
        if packet.Spin.CurrentStage == pb.Slot.Stage.BASE:
            self.life -= 1
            if self.life % 1000 == 0:
                self.print_user_data()

    def prepare(self):
        self.req_login()
        self.enter_theme()

    def run(self):
        while self.life > 0:
            # self.spin()
            self.controller.do_play(robot)
        pass