#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

demon_theme_id = 10040

class FortuneRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, demon_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        self.log_spin_wins(packet.Spin)
        pass

def run(player):
    # player.send_cmd(add_money)
    # player.select_bet(40000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()

    # player.send_cmd(cheat_6)
    # player.send_cmd(test_gm)

    # player.send_gm(enter_pick)
    # player.spin()
    # player.pick(0)

    # player.send_gm(enter_pick)
    # player.spin()
    # player.pick(1)

    player.spin_to_base()
    # player.spin()
    # player.spin_times(3)

  
    # player.send_cmd(demon_panelgroup)
    pass

add_money = "add coin 9999999"
enter_pick = "2_200|4;"
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