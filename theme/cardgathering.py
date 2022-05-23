#! /usr/bin/env
#coding=utf-8

import msg
import gen.proto as pb
from robot import SpinRobot

fortune_theme_id = 10040
add_card_all = "cardadd"
add_card_one = "cardadd 1 1"


class CardGathering(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, fortune_theme_id)

    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass

    def on_cardgathering(self, packet):
        if packet.HasField("UserData"):
            # userData = pb.CardGathering.Data()
            # userData.UserData = pb.CardGathering.UserData()
            # userData.UserData = packet.UserData.Data.UserData
            # userData.CardDeckList = packet.UserData.Data.CardDeckList
            # userData.CardList = packet.UserData.Data.CardList
            # self.log(userData)
            
            # self.log(packet.UserData.Data.CardDeckList)
            # self.log(packet.UserData.Data.CardList)
            # self.log(packet.UserData.Data.UserData)

            # packet.UserData.Data.CardLogList = pb.CardGathering.Data.CardLogList.add()

            self.log(packet.UserData.Data)


gem_cmd = "add gem 9999999"
all_card_cmd = "cardadd"
cost_cmd = "cardadd 0,16"
cost_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def run(player):
    player.send_cmd(add_card_all)

    player.req_cardgathering_data(0)
    # player.req_cardgathering_exchange(2, 5)

    # player.send_cmd(gem_cmd)
    # player.req_cardgathering_reset()


    # player.send_cmd(cost_cmd)
    # player.req_cardgathering_break(0, cost_cards)
    

    pass