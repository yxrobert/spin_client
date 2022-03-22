#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot

demon_theme_id = 10130

class DemonRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, demon_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        # self.log(packet.Spin.SymbolList)
        pass

    


def run(player):
    # player.select_bet(40000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()
    # player.spin_to_base()
    # player.send_cmd(cheat_6)
    # player.send_cmd(panic_cmd2)
    player.spin()
    # player.pick(1)
    # player.send_cmd(demon_panelgroup)
    pass

# grorilla_3sc = "panels 1_5_7_9_9_9_9_9_1_9_9_9_9_9_9_9_1_9_9_9"
demon_panelgroup = "panelgroup 1_1_1_2_2_2_3_3_3_3_3_3_3_3_3|1_1_1_2_2_2_3_3_3_3_3_3_3_3_3"
cheat_6 = "math:6"
panic_cmd2 = "panelgroup 4_4_4_3_3_3_0_0_0_0_0_0_0_0_0|4_4_4_3_3_3_0_0_0_0_0_0_0_0_0"
panic_cmd3 = "panelgroup 4_4_4_3_3_3_0_0_0_0_0_0_0_0_0|4_4_4_3_3_3_0_0_0_0_0_0_0_0_0|4_4_4_3_3_3_0_0_0_0_0_0_0_0_0"


# def run_gm(player):
#     player.send_cmd(theme.cheat_6)

#     # gorilla
#     # player.send_cmd(grorilla_3sc)

#     pass

def main():
	pass

if __name__ == '__main__':
	main()