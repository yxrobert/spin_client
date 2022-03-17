#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot


cheat_6 = "cheat 6"
cheat_12 = "cheat 12"
add_money = "add coin 9999999"

class DefaultRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass


def default_spin_callback(packet):
    msg.log_spin(packet)
    # msg.log_jpvision(packet)
    pass

def default_theme_callback(packet):
    # msg.log_piggy_theme(packet)
    # msg.log_theme_jpvision(packet)
    # msg.log_theme_lastrsp(packet)
    pass

def run(player):
    player.req_activity_list()
    player.req_activity_user_data(3)
    player.req_activity_user_data(1)
    player.req_activity_play(1)

    # player.select_bet(40000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()
    # player.spin_to_base()
    # player.spin()
    # player.pick(1)
    pass