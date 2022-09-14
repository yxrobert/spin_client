#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

demon_theme_id = 10150

class LuckRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, demon_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        self.log_spin_wins(packet.Spin)
        pass

def run(player):
    # player.select_bet(40000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()

    # player.send_cmd(cheat_free)
    # player.send_cmd(cheat_free)
    # player.send_cmd(cheat_6)
    # player.send_cmd(test_gm)
    # player.send_cmd(rtp_150)

    # player.send_cmd(cheat_free)
    # player.send_cmd(cheat_58)
    player.spin()
    # player.spin_to_base()

    # player.pick(1)
    # player.send_cmd(demon_panelgroup)
    pass

rtp_150 = "rtpf 150"
cheat_free = "math:55"
p_cmd = "panel 11,11,1,1,1,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,3,3,3,3,3"


glcoin = "glcoin 99999"
free_cmd = "panel 1,1,2,8,0,0,0,0,0,0,0,0,1,1,1,1,9,9,9,4"
test_gm = "gm:2_200|2;1_100|2_3_7"
cheat_6 = "cheat 6"
# test_gm = "gm:2_200|2;"
# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
# demon_panelgroup = "panelgroup 1_1_1_2_2_2_3_3_3_3_3_3_3_3_3|1_1_1_2_2_2_3_3_3_3_3_3_3_3_3"
cheat_6 = "math:6"
cheat_58 = "math:58"
cheat_54 = "math:54"
cheat_56 = "math:56"


def main():
	pass

if __name__ == '__main__':
	main()