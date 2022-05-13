#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

fortune_theme_id = 10040

class CardGathering(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, fortune_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass

def run(player):
    print("CardGathering")
    player.req_cardgathering_data(0)
    pass