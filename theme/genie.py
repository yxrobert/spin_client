#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot
from common import *

genie_theme_id = 10030

class GenieRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, genie_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        self.log_spin_wins(packet.Spin)
        pass

def run(player):
    # player.select_bet(40000)
    # player.send_cmd(cheat_12)
    # player.send_cmd(add_money)
    player.spin_to_next_stage()


    # player.send_cmd(free_cmd)
    # player.send_cmd(test_gm2)
    # player.spin()
    # player.pick(0)

    # player.spin()
    # player.spin_times(10)
    # player.spin_to_base()

    # player.pick(0)
    # player.send_cmd(demon_panelgroup)

    # for i in range(0, 30):
    #     player.spin()
    #     player.pick(0)
    pass

free_cmd = "gm:2_200|4"
test_gm = "gm:2_200|2;1_100|2_3_7"
cheat_6 = "cheat 6"
test_gm2 = "gm:0_0|2_6_11>0_0|2_15_11;0_4|2_1_2;0_4|2_1_3;0_4|2_1_4"
# test_gm = "gm:2_200|2;"
# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
# demon_panelgroup = "panelgroup 1_1_1_2_2_2_3_3_3_3_3_3_3_3_3|1_1_1_2_2_2_3_3_3_3_3_3_3_3_3"
# cheat_6 = "math:6"


def main():
	pass

if __name__ == '__main__':
	main()