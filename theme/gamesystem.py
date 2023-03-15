#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot
from net import Sender


add_money = "add coin 99999999999"

class SystemRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, 10040)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass

    def default_spin_callback(packet):
        msg.log_spin(packet)
        # msg.log_jpvision(packet)
        pass

    def default_theme_callback(packet):
        # msg.log_piggy_theme(packet)
        # msg.log_theme_jpvision(packet)
        # msg.log_theme_lastrsp(packet)
        pass

    def run(player):
        for i in range(0,7):
            player.req_magic_play(0, i)
        # print("req bonus")
        # player.req_bonus(2,2)
        pass

basebet_cmd="basebet"
free_me = "freeme"
xpay = "xpay 10000 1"
gmnow = "now"
journey = "journey 1,100"
journey_roll = "jroll 50"
dice_cmd = "add dice 999999"
candy_cmd = "add candy 999999"
level_cmd = "add level 100"
lv10_cmd = "add level 10"
coin_cmd = "add coin 99999999"
gem_cmd = "add gem 99999999"
candy_cmd = "add candy 99999999"
bingoball_cmd = "add bingoBall 999999"
bingo_bp = "bgboxpass"
bingo_pro_cmd = "bgaddp 10000"
mock_time="st:2022-04-09 14:02:00"

cmd_lj="rpanel 1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5"