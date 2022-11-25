#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

demon_theme_id = 10020

class VegasRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, demon_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        self.log_spin_wins(packet.Spin)
        pass

def run(player):
    # player.select_bet(400000)
    # player.send_cmd("rtpf 55")
    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()

    # player.send_cmd(cheat_6)
    # player.send_cmd(test_gm)

    player.spin_to_base()
    player.send_cmd(gm_bonus_jp)
    # player.send_cmd(free_cmd)
    player.spin()
    player.spin_to_base()

    # player.pick(1)
    # player.send_cmd(demon_panelgroup)
    pass

gm_bonus_jp = "0_0|0_3_9>0_1|2_4_1_14;0_1|2_1_4_10>5_500|2_1_1_14>5_500|2_2_1_14>5_500|2_3_1_14>5_500|2_4_1_14"
gm_jp = "gm:0_0|0_3_9>0_1|2_4_3_13;0_1|2_1_4_10"
free_cmd = "panel 1,1,2,8,0,0,0,0,0,0,0,0,1,1,1,1,9,9,9,4"
test_gm = "gm:2_200|2;1_100|2_3_7"
cheat_6 = "cheat 6"
# test_gm = "gm:2_200|2;"
# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
# demon_panelgroup = "panelgroup 1_1_1_2_2_2_3_3_3_3_3_3_3_3_3|1_1_1_2_2_2_3_3_3_3_3_3_3_3_3"
# cheat_6 = "math:6"


def main():
	pass

if __name__ == '__main__':
	main()