#! /usr/bin/env
#coding=utf-8

import httplib, time
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

    10130 : [theme.DemonRobot, theme.demon.run],
    10090 : [theme.TrainRobot, theme.train.run],
    10020 : [theme.VegasRobot, theme.vegas.run],
    10040 : [theme.FortuneRobot, theme.fortune.run],
    10030 : [theme.GenieRobot, theme.genie.run],
    10150 : [theme.LuckRobot, theme.potoluck.run],
    10110 : [theme.IcePrincessRobot, theme.iceprincess.run],

    1 : [theme.CardGathering, theme.cardgathering.run],
    2 : [theme.LevelSprint, theme.levelsprint.run],
    10 : [theme.SystemRobot, theme.SystemRobot.run],
    100 : [theme.FuncRobot, theme.functions.run],
    }

def create_theme_robot(theme_id):
    robot_name = conf.get_account()
    if tab_theme_robot.has_key(theme_id):
        return robot.robot_init(tab_theme_robot[theme_id][0](robot_name, theme_id)), tab_theme_robot[theme_id][1]
    else:
        return robot.robot_init(theme.DefaultRobot(robot_name, theme_id)), theme.common.run


def run(theme_id):
    url = conf.get_svr_url()
    print(url)
    Sender.set_server_addr(url)
    player, run_func = create_theme_robot(theme_id)

    # load conf
    player.select_bet(int(conf.get_default_bet()))
    player.set_auto_interval(float(conf.get_interval()))

    run_func(player)
    
def md5_str():
    print(abs(hash("1673085562#5009001659698033#JJJUCPFAXYHLKD7U#10006#ifun_game_email_push")))


def main():
    # for i in range(10):
    #     md5_str()
    #     time.sleep(1)
    # return
    if len(sys.argv) <= 1:
        print("select theme")
        return

    theme_id = int(sys.argv[1])
    run(theme_id)


if __name__ == '__main__':
	main()