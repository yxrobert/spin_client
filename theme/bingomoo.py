#! /usr/bin/env
#coding=utf-8

import msg
import gen.proto as pb
from robot import SpinRobot

bingoMoo_theme_id = 10050

class BingoMooRobot(SpinRobot):
    def __init__(self, name, theme_id):
        SpinRobot.__init__(self, name, bingoMoo_theme_id)

    def theme_status_callback(self, packet):
        log_packet = pb.ThemeStatus()

        log_packet.bingoMoo.Data.CurType = packet.bingoMoo.Data.CurType
        log_packet.bingoMoo.Data.AverageBets = packet.bingoMoo.Data.AverageBets
        log_packet.bingoMoo.Data.Progress = packet.bingoMoo.Data.Progress
        log_packet.bingoMoo.Data.TriggerBet = packet.bingoMoo.Data.TriggerBet

        # log_packet.bingoMoo.Data.ClearField("FeatureBingoPanel")
        # log_packet.bingoMoo.Data.ClearField("BingoPanelArr")
        # print(packet.LastResponses)

        # self.log(msg.log_theme_lastrsp(packet))
        # self.log(log_packet)

        # self.log(log_bingomoo(packet))

    def play_status_callback(self, packet):
        self.log(log_bingomoo(packet))
        pass

def log_bingomoo(packet):
    log_packet = pb.PlayResponse()
    # log_packet.bingoMoo.Data.ClearField("FeatureBingoPanel")
    # log_packet.bingoMoo.Data.ClearField("BingoPanelArr")
    # print(packet.Spin.bingoMoo)
    log_packet.Spin.bingoMoo.CurType = packet.Spin.bingoMoo.CurType
    log_packet.Spin.bingoMoo.Progress = packet.Spin.bingoMoo.Progress
    log_packet.Spin.bingoMoo.AverageBets = packet.Spin.bingoMoo.AverageBets
    log_packet.Spin.bingoMoo.TriggerBet = packet.Spin.bingoMoo.TriggerBet

    # for i in packet.Spin.bingoMoo.BingoPanelArr:
    #     i.ClearField("BingoPanel")
    #     log_packet.Spin.bingoMoo.BingoPanelArr.append(i)

    return log_packet


bingomoo_free = "0_0|2_3_15"
bingomoo_free_cmd = "gm:0_0|2_3_15"
bingomoo_mega = "eval FeatureProgress_11"
bingomoo_supper = "eval FeatureProgress_17"

chain = "chain"

def run_mege(player):
    # player.send_cmd(chain)
    # average bet
    # player.select_bet(200000)
    player.spin()
    # player.select_bet(20000)
    # player.spin_times(1)


    # gm
    # player.select_bet(20000)
    # player.spin_to_base()
    # player.spin()

    # player.send_cmd(bingomoo_mega)
    # player.send_cmd(bingomoo_supper)
    # player.send_gm(bingomoo_free)
    # player.spin()
    # player.spin_to_next_stage()

    # player.spin_to_base()
    pass

def run(player):
    player.select_bet(20000)
    # player.spin()
    player.spin_to_next_stage()
    # player.spin_to_base()

    # player.send_gm(bingomoo_free)
    # player.send_cmd(bingomoo_supper)

    # player.send_cmd(theme.cheat_6)
    pass

def main():
	pass

if __name__ == '__main__':
	main()