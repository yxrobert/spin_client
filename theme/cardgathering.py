#! /usr/bin/env
#coding=utf-8

import gen.proto as pb
import msg
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
cost_cards = [90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]

def gm_card(player):
    cards = [2,3,4,5,6,7,8,9,10, 12,13,14,15,16,17,18,19,20, 22,23,24,25,26,27,28,29,30, 32,33,34,35,36,37,38,39,40, 42,43,44,45,46,47,48,49,50, 52,53,54,55,56,57,58,59,60, 62,63,64,65,66,67,68,69,70, 82,83,84,85,86,87,88,89,90, 92,93,94,95,96,97,98,99,100, 102,103,104,105,106,107,108,109,110, 112,113,114,115,116,117,118,119,120]
    for c in cards:
        player.send_cmd("cardadd " + str(c)+ " 1")
    pass


def run(player):
    # player.send_cmd(add_card_all)
    # player.send_cmd("cardadd 122 1")

    # player.req_cardgathering_data(-1)
    # player.req_cardgathering_exchange(122, 50)
    # player.req_cardgathering_gameaward()

    # player.send_cmd(gem_cmd)
    # player.req_cardgathering_reset()


    # player.send_cmd("cardreset")
    # player.send_cmd("cardadd 90,15")
    # player.req_cardgathering_break(2, cost_cards)
    player.req_cardgathering_gameaward()

    # gm_card(player)
    # player.spin()
    # player.req_cardgathering_data(-1)
    pass
