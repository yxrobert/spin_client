#! /usr/bin/env
#coding=utf-8

import gen.proto as pb

def log_wins(packet):
    log_packet = pb.SpinResponse()
    log_packet.PanelWins = packet.PanelWins
    log_packet.FeatureWins = packet.FeatureWins
    log_packet.SpinWins = packet.SpinWins
    log_packet.PCWins = packet.PCWins
    log_packet.PlayCycleWins.TriggerWins = packet.PlayCycleWins.TriggerWins
    log_packet.PlayCycleWins.TotalWins = packet.PlayCycleWins.TotalWins

    return log_packet

def log_spin(packet):
    log_packet = pb.PlayResponse()

    log_packet.Spin.CurrentStage = packet.Spin.CurrentStage
    log_packet.Spin.NextStage = packet.Spin.NextStage
    log_packet.Spin.TotalBet = packet.Spin.TotalBet

    print(log_packet)

def log_picker(packet):
    print(packet.Spin.Picker)

def log_left_times(packet):
    print(packet.Spin.leftTimes)

def log_jpvision(packet):
    print(packet.Spin.JPVisions)
    pass 


def log_gorilla(packet):
    log_packet = pb.PlayResponse()

    log_packet.Spin.gorilla.Coins = packet.Spin.gorilla.Coins
    log_packet.Spin.gorilla.FeatureN = packet.Spin.gorilla.FeatureN
    log_packet.Spin.gorilla.CollectN = packet.Spin.gorilla.CollectN
    log_packet.Spin.gorilla.CollectCoin = packet.Spin.gorilla.CollectCoin
    log_packet.Spin.gorilla.TriggerFrom = packet.Spin.gorilla.TriggerFrom

    print(log_packet)

def log_piggy(packet):
    log_packet = pb.PlayResponse()

    log_packet.Spin.piggyBank.CurType = packet.Spin.piggyBank.CurType
    log_packet.Spin.piggyBank.Progress = packet.Spin.piggyBank.Progress
    log_packet.Spin.piggyBank.BetLimit = packet.Spin.piggyBank.BetLimit
    log_packet.Spin.piggyBank.AverageBets = packet.Spin.piggyBank.AverageBets
    # log_packet.Spin.piggyBank.StepperData = packet.Spin.piggyBank.StepperData
    # log_packet.Spin.piggyBank.TriggerSymbolList = packet.Spin.piggyBank.TriggerSymbolList
    print(log_packet)


def log_bingomoo(packet):
    log_packet = pb.PlayResponse()

    # log_packet.bingoMoo.Data.ClearField("FeatureBingoPanel")
    # log_packet.bingoMoo.Data.ClearField("BingoPanelArr")
    # print(packet.Spin.bingoMoo)

    log_packet.Spin.bingoMoo.CurType = packet.Spin.bingoMoo.CurType
    log_packet.Spin.bingoMoo.Progress = packet.Spin.bingoMoo.Progress
    log_packet.Spin.bingoMoo.AverageBets = packet.Spin.bingoMoo.AverageBets
    print(log_packet)


def main():
    pass

if __name__ == '__main__':
	main()