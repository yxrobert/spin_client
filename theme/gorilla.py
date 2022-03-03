#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

class GorillaRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass


def run(player):
    # player.select_bet(40000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()
    # player.spin_to_base()
    player.spin()
    # player.pick(1)
    pass

# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"

# def run_gm(player):
#     player.send_cmd(theme.cheat_6)

#     # gorilla
#     # player.send_cmd(grorilla_3sc)

#     pass

def main():
	pass

if __name__ == '__main__':
	main()