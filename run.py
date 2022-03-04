#! /usr/bin/env
#coding=utf-8

import httplib
import sys

from net import Sender
import robot
import msg
import gen.proto as pb
import theme
import conf

# run func
tab_theme_robot = {
    10050 : [theme.BingoMooRobot, theme.bingomoo.run],
    10051 : [theme.BingoMooRobot, theme.bingomoo.run_mege],

    10070 : [theme.PiggyRobot, theme.piggybank.run],
    10080 : [theme.GorillaRobot, theme.gorilla.run],
    }

def create_theme_robot(theme_id):
    robot_name = conf.get_account()
    if tab_theme_robot.has_key(theme_id):
        return robot.robot_init(tab_theme_robot[theme_id][0](robot_name, theme_id)), tab_theme_robot[theme_id][1]
    else:
        return robot.robot_init(theme.DefaultRobot(robot_name, theme_id)), theme.common.run


def run(theme_id):
    Sender.set_server_addr(conf.get_svr_url())
    player, run_func = create_theme_robot(theme_id)

    # load conf
    player.select_bet(int(conf.get_default_bet()))
    player.set_auto_interval(float(conf.get_interval()))

    run_func(player)
    


def main():
    if len(sys.argv) <= 1:
        print("select theme")
        return

    theme_id = int(sys.argv[1])
    run(theme_id)


if __name__ == '__main__':
	main()