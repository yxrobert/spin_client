#! /usr/bin/env
#coding=utf-8

import msg
from common import *
from robot import SpinRobot

piggy_theme_id = 10070

class PiggyRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, piggy_theme_id)

    def theme_status_callback(self, packet):
        self.log(msg.log_piggy_theme(packet))

    def play_status_callback(self, packet):
        self.log(msg.log_piggy(packet))


piggy_free = "0_0|0_2_7"
piggy_supper = "eval FeatureProgress_9"

piggy_stepper = "panels 18_14_14_19_14_14_20_14_14_21_14_14_22_14_14|23_2_23_23_2_23_23_2_23"
pg_yue = "panels 18_18_18_19_19_19_20_20_20_21_21_21_22_22_22"
pg_yq = "panel 7,8,8,7,7,9,6,6,6,6,6,6,6,6,6"


def run(player):
    # player.send_cmd(add_money)
    player.spin_to_next_stage()
    # player.spin_to_base()

    # player.send_gm(piggy_free)
    # player.send_cmd(piggy_supper)
    # player.send_cmd(pg_yq)

    # player.send_cmd(theme.cheat_6)
    # player.send_cmd(piggy_stepper)

    # for i in range(0, 10):
    #     player.spin()
    # player.spin_to_base()

    pass

def main():
	pass

if __name__ == '__main__':
	main()