#! /usr/bin/env
#coding=utf-8

from robot import SpinRobot
import gen.proto as pb
import net

class PreRobot(SpinRobot):
    def __init__(self, addr, name, theme_id, life):
        SpinRobot.__init__(self, name, theme_id)
        self.life = int(life)
        self.set_auto_interval(0.001)
        self.log_switch = False
        self.transportor = net.Transportor(addr)

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

    def on_response(self, packet):
        if packet.Error != None:
            self.process_err(packet.Error)
            self.err_count += 1
            self.log_err("err_count:%d" % self.err_count)

        if packet.HasField("Login"):
            self.on_login(packet)
            return

        for r in packet.Multi.Responses:
            if r.HasField("ThemeStatus"):
                self.on_theme_status(r.ThemeStatus)
            elif r.HasField("Play"):
                pass
        
    def on_play(self, packet):
        self.themeData.update_from_play(packet)
        # self.log("on_play")
        # self.themeData.show_stage()
        # print(packet.Spin.CurrentStage)
        # print(pb.Slot.Stage.BASE)
        if packet.Spin.CurrentStage == pb.Slot.Stage.BASE:
            self.life -= 1
            print(self.life)

    def prepare(self):
        self.req_login()
        self.enter_theme()

    def run(self):
        # self.req_login()
        # self.send_cmd("add coin 9999999")
        # self.send_cmd("setlevel 50")

        # self.enter_theme()
        while self.life > 0:
            self.spin()
        pass