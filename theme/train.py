#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot
from common import *

demon_theme_id = 10250

class TrainRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, demon_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        # self.log(packet.Spin.SymbolList)
        self.log_spin_wins(packet.Spin)
        pass

def run(player):
    # player.select_bet(120000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()
    # player.send_cmd(test_gm)

    # player.send_cmd(panels_yq)
    # player.send_cmd(gm_enter)
    # player.send_cmd(add_money)
    # player.send_cmd("add level 11")
    # player.send_cmd("bgdrop 4")

    player.spin_times(1)
    # player.spin_to_base()
    # player.spin_to_next_stage()

    # player.pick(1)
    # player.send_cmd(demon_panelgroup)
    pass

panels = '''panelstr [[{"ss":[{"s":4},{"s":11,"t":5},{"s":11,"t":6}]},{"ss":[{"s":7},{"s":11,"t":4},{"s":12,"t":3}]},{"ss":[{"s":7},{"s":2},{"s":2}]},{"ss":[{"s":5},{"s":3},{"s":4}]},{"ss":[{"s":2},{"s":7},{"s":7}]}],[{"ss":[{"s":4},{"s":11,"t":5},{"s":11,"t":6}]},{"ss":[{"s":7},{"s":11,"t":4},{"s":12,"t":3}]},{"ss":[{"s":7},{"s":2},{"s":2}]},{"ss":[{"s":5},{"s":3},{"s":4}]},{"ss":[{"s":2},{"s":7},{"s":7}]}]]'''
panels_yq = '''panelstr [[{"ss":[{"s":7},{"s":11,"t":5},{"s":11,"t":6}]},{"ss":[{"s":7},{"s":11,"t":4},{"s":12,"t":3}]},{"ss":[{"s":7},{"s":2},{"s":2}]},{"ss":[{"s":5},{"s":3},{"s":4}]},{"ss":[{"s":2},{"s":7},{"s":7}]}]]'''

gm_free = "gm:2_200|2;0_0|0_0_12"
test_gm = "gm:2_200|2;1_100|2_3_7"
cheat_6 = "cheat 6"

gm_enter = "gm:cmd:collectionex:0_0|0_0_8"
# test_gm = "gm:2_200|2;"
# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
# demon_panelgroup = "panelgroup 1_1_1_2_2_2_3_3_3_3_3_3_3_3_3|1_1_1_2_2_2_3_3_3_3_3_3_3_3_3"
# cheat_6 = "math:6"


# def run_gm(player):
#     player.send_cmd(theme.cheat_6)

#     # gorilla
#     # player.send_cmd(grorilla_3sc)

#     pass

def main():
	pass

if __name__ == '__main__':
	main()