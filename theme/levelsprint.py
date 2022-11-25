#! /usr/bin/env
#coding=utf-8

import gen.proto as pb
import msg
from robot import SpinRobot

fortune_theme_id = 10040

class LevelSprint(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, fortune_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass

    # def on_cardgathering(self, packet):
    #     if packet.HasField("UserData"):
    #         self.log(packet.UserData.Data)



def run(player):
    # player.send_cmd(add_card_all)
    # player.send_cmd("lsgame")
    # player.send_cmd("add level 30")

    # player.req_levelsprint_draw()
    player.req_levelsprint_get()

    # player.spin()
    # player.req_cardgathering_data(-1)
    pass
