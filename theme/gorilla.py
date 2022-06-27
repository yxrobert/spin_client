#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

# gorilla_theme_id = 10080
gorilla_theme_id = 10140

class GorillaRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, gorilla_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        # self.log_spin_wins(packet.Spin)
        self.log(msg.log_gorilla(packet))
        pass


def run(player):
    # player.select_bet(40000)

    # player.send_cmd(glcoin)
    # for i in range(0, 9):
    #     player.game(0, i)

    # player.spin_to_next_stage()
    # player.spin()
    # player.pick(0)
    # player.spin_to_base()
    # player.spin()
    # player.pick(1)
    # player.send_cmd(grorilla_panelgroup)
    player.send_cmd(test_ln)
    pass

test_ln="rpanel 2,2,2,10,10,10,2,2,2,10,10,10,2,2,2,2,2,2,2,2,2,10,10,10,2,2,2,10,10,10"
free = "gm:cmd:randpanels {*:4-13}_{-|:1}1_5_*_*_1_5_*_*_1_5_*_*_*_5_*_*_*_5_*_*"
glcoin = "glcoin 99999"
# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
grorilla_panelgroup = "panelgroup 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9|1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"

# def run_gm(player):
#     player.send_cmd(theme.cheat_6)

#     # gorilla
#     # player.send_cmd(grorilla_3sc)

#     pass

def main():
	pass

if __name__ == '__main__':
	main()