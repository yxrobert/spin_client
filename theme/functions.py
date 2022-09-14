#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot
from net import Sender


cheat_6 = "cheat 6"
cheat_12 = "cheat 12"
add_money = "add coin 99999999999"

class FuncRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, 10040)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass


def default_spin_callback(packet):
    msg.log_spin(packet)
    pass

def default_theme_callback(packet):
    pass

hero1 = "hero1"
free_item = "heroFreeActiveItem"

def run(player):
    player.req_hero_active(hero1, free_item)

    pass