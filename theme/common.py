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

    def on_act_play(self, packet):
        pass

    def on_act_userdata(self, packet):
        msg.log_act_all(self, packet)

    def on_act_play(self, packet):
        msg.log_act_all(self, packet)



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

def gm_meta(player):
    player.send_cmd("metaj 0,6")
    # player.send_cmd("metap")
    player.send_cmd("metas")

    # player.send_cmd("candypop 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2")

    pass

def run(player):
    # player.req_novice_save(1)
    # return 
    # player.send_cmd("panelm 1,2,3;1,2,3,4;1,2,3,4,5|1,2,3;1,2,3,4;1,2,3,4,5")
    # player.send_cmd(candy_cmd)
    # player.send_cmd(gem_cmd)
    # player.send_cmd(add_money)
    # player.send_cmd("currency coin,1111")
    # player.send_cmd("pgto 120")
    # player.send_cmd("pgreset")
    # player.send_cmd(xpay)
    # player.send_cmd(free_me)
    # player.send_cmd(cmd_lj)
    
    # player.send_cmd(basebet_cmd)
    # player.send_cmd(coin_cmd)
    # player.send_cmd(level_cmd)
    # player.send_cmd(bingo_bp)
    player.send_cmd(lv10_cmd)
    # gm_meta(player)

    # player.send_cmd(dice_cmd)
    # player.send_cmd(candy_cmd)
    # player.send_cmd(bingoball_cmd)
    # player.send_cmd(bingo_pro_cmd)
    # player.send_cmd(gmnow)
    # player.send_cmd(journey_roll)
    # player.send_cmd("journey 0,118")
    # player.send_cmd("jroll 20")
    
    # player.req_treasure_get()
    # player.req_activity_list()

    # player.send_cmd("metaj 0,1")
    # player.send_cmd("metas")

    # player.send_cmd("trs")
    # player.send_cmd("bgboxpass")
    # player.send_cmd("trmail")
    # player.send_cmd("maildrop 56002")

    # act_id = 113
    act_id = 146
    player.req_activity_user_data(act_id)
    times = 1
    for i in range(0, times):
        player.req_activity_play(act_id)
        pass
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