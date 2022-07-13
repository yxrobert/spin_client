#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

fortune_theme_id = 10040

class FortuneRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, fortune_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        self.log_spin_wins(packet.Spin)
        pass


def run(player):
    player.send_cmd(add_money)
    player.select_bet(60000000)

    # player.send_cmd(bonus)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()

    # player.send_cmd(add_money)
    # player.send_cmd(test_gm)
    # player.send_cmd("freeme")

    # player.send_gm(add_money)
    # player.spin()
    # player.pick(0)

    # go_money_pick(player, 0)
    # go_pick(player, 0)

    # player.send_gm(jackpot)
    # player.send_gm("freeme")
    # player.send_gm(enter_pick)
    # player.spin()
    # player.pick(0)
    # player.serials_game(jp_arr)

    # player.spin_to_base()
    player.spin()
    # player.spin_times(30)

  
    # player.send_cmd(demon_panelgroup)
    pass

def go_money_pick(player, idx):
    player.send_cmd(money_pick)
    player.spin()
    player.pick(idx)
    player.spin_to_base()


def go_pick(player, idx):
    player.send_gm(enter_pick)
    player.spin()
    player.pick(idx)
    player.spin_to_base()


jp_arr = [0,1,2,3,4,5,6,7,8]
# jp_arr = [9]

jackpot = "gm:0_0|0_0_0;7_1000|1;7_1000|4_1_3_2_4_4_2_1_1_3_2_3"
add_money = "add coin 9999999"
enter_pick = "2_200|4;"
test_gm = "gm:2_200|2;1_100|2_3_7"
cheat_6 = "cheat 6"
money_pick = "panel 3,4,2,3,5,6,3,10,10,3,10,10,3,10,10"
bonus="randpanels {*:2-9}_{#:11_12}10_10_10_10_10_10_*_*_*_*_*_*_*_*_*|*_*_*_*_*_*_#_#_#_#_#_#_#_#_*|*_*_*_*_*_*_*_*_*_*_*_*_*_*_#"
# test_gm = "gm:2_200|2;"
# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
# demon_panelgroup = "panelgroup 1_1_1_2_2_2_3_3_3_3_3_3_3_3_3|1_1_1_2_2_2_3_3_3_3_3_3_3_3_3"
# cheat_6 = "math:6"


def main():
	pass

if __name__ == '__main__':
	main()