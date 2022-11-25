#! /usr/bin/env
#coding=utf-8

from robot import SpinRobot
import gen.proto as pb

class PreRobot(SpinRobot):
    def __init__(self, name, theme_id, life):
        SpinRobot.__init__(self, name, theme_id)
        self.life = int(life)
        self.set_auto_interval(0.001)

    def on_response(self, packet):
        if packet.Error != None:
            self.process_err(packet.Error)

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