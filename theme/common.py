#! /usr/bin/env
#coding=utf-8

import msg
from robot import SpinRobot
from net import Sender


cheat_6 = "cheat 6"
cheat_12 = "cheat 12"
add_money = "add coin 99999999999"

class DefaultRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, 10040)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass

    # def on_activity(self, packet):
    #     # self.log(111111)
    #     # if packet.HasField("Play"):
    #     #     self.log(packet.Play.data.Bingo)
    #         # if packet.Play.data.HasField("Bingo"):
    #         #     d = packet.Play.data.Bingo
    #         #     self.log(111111)
    #         #     self.log(p)
    #     pass


def default_spin_callback(packet):
    msg.log_spin(packet)
    # msg.log_jpvision(packet)
    pass

def default_theme_callback(packet):
    # msg.log_piggy_theme(packet)
    # msg.log_theme_jpvision(packet)
    # msg.log_theme_lastrsp(packet)
    pass

def fakeTIme():
    Sender.send_timefake("11111")

def run(player):
    # player.send_cmd(gem_cmd)
    # player.send_cmd(add_money)
    # player.send_cmd(free_me)
    
    # player.send_cmd(coin_cmd)
    # player.send_cmd(level_cmd)
    # player.send_cmd(lv10_cmd)
    # player.send_cmd(dice_cmd)
    # player.send_cmd(bingoball_cmd)
    # player.send_cmd(gmnow)
    # player.send_cmd(journey_roll)
    
    player.req_activity_list()

    act_id = 1
    # player.req_activity_user_data(act_id)
    # for i in range(0, 10):
        # player.req_activity_play(act_id)
    # player.req_activity_play(act_id)

    # player.send_cmd(dice_cmd)
    # player.send_cmd(journey)
    # player.send_cmd(journey)


    # player.select_bet(40000)

    # player.send_cmd(cheat_12)
    # player.spin_to_next_stage()
    # player.spin_to_base()
    # player.spin()
    # player.pick(1)
    pass

free_me = "freeme"
gmnow = "now"
journey = "journey 0,100"
journey_roll = "jroll 50"
dice_cmd = "add dice 999999"
level_cmd = "add level 100"
lv10_cmd = "add level 10"
coin_cmd = "add coin 99999999"
gem_cmd = "add gem 99999999"
bingoball_cmd = "add bingoBall 999999"
mock_time="st:2022-04-09 14:02:00"