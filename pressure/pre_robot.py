#! /usr/bin/env
#coding=utf-8

from robot import SpinRobot
import gen.proto as pb
from net import *
from controller import ThemeController
from tiki import Tiki
from genie import Genie
from fortune import Fortune
import time

theme_register = {
    # default theme
    # [10090, 10020]
    10290 : Tiki,
    10030 : Genie,
    10040 : Fortune,
}

def create_theme_controller(theme_id):
    if theme_register.has_key(theme_id):
         return theme_register[theme_id](theme_id)   
    else:
        return ThemeController(theme_id)

class PreRobot(SpinRobot):
    def __init__(self, addr, name, theme_id, spin_quest):
        SpinRobot.__init__(self, name, theme_id)
        self.spin_quest = int(spin_quest)
        self.quest_interval = self.spin_quest / 3
        self.set_auto_interval(0.001)
        self.log_switch = False
        self.transportor = Requester(addr)
        # self.transportor = Transportor(addr)
        self.controller = create_theme_controller(theme_id)
        self.start_time = int(time.time())
        self.is_login = False

    def get_life(self):
        return int(time.time()) - self.start_time

    def print_user_data(self):
        self.log("[name:%s uid:%d token:%s theme:%d spin_quest:%d life:%d(s)] speed:%.4f" 
            % (self.name, self.player_id, self.token, self.theme_id, self.spin_quest, self.get_life(), self.transportor.get_speed()))

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
        self.is_login = True
        self.print_user_data()     

    def on_response(self, packet):
        # print("on_response")
        if packet.Error != None and len(packet.Error.Msg) > 0:
            self.process_err(packet.Error)
            self.err_count += 1
            self.log_err("[code:%d] [mgs:%s]err_count:%d" % (packet.Error.Code, packet.Error.Msg, self.err_count))
            return

        if ~self.is_login and packet.HasField("Login"):
            self.on_login(packet)
            return

        for r in packet.Multi.Responses:
            if r.HasField("Play"):
                self.on_play(r.Play)
                self.controller.handle_play(r.Play)
            elif r.HasField("ThemeStatus"):
                self.on_theme_status(r.ThemeStatus)
                self.controller.handle_theme_status(r.ThemeStatus)
            
    def on_play(self, packet):
        self.themeData.update_from_play(packet)
        if packet.Spin.CurrentStage == pb.Slot.Stage.BASE:
            self.spin_quest -= 1
            if self.spin_quest % self.quest_interval == 0:
                self.print_user_data()

    def prepare(self):
        self.req_login()
        self.enter_theme()

    def run(self):
        while self.spin_quest > 0:
            # self.spin()
            self.controller.do_play(self)
        pass