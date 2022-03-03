#! /usr/bin/env
#coding=utf-8

import gen.proto as pb

def log_theme_status(packet):
    log_packet = pb.ThemeStatus()
    log_packet.CurrentStage = packet.CurrentStage
    log_packet.NextStage = packet.NextStage
    log_packet.LastBet = packet.LastBet

    if packet.HasField("Respin"):
        log_packet.Respin.RemainTimes = packet.Respin.RemainTimes
        log_packet.Respin.TotalTimes = packet.Respin.TotalTimes
        log_packet.Respin.TriggerWin = packet.Respin.TriggerWin

    if packet.HasField("Freespin"):
        log_packet.Freespin.RemainTimes = packet.Freespin.RemainTimes
        log_packet.Freespin.TotalTimes = packet.Freespin.TotalTimes
        log_packet.Freespin.TriggerWin = packet.Freespin.TriggerWin

    return log_packet

def log_theme_jpvision(packet):
    print(packet.JPVisions)
    pass 

def log_theme_lastrsp(packet):
    print(packet.LastResponses)
    pass 

def log_lastrsp_bet(packet):
    print(packet.LastResponses)
    # for i in packet.LastResponses:
        # print("lastrsp \n")
        # print(i)

def log_theme_free(packet):
    if packet.Freespin != None:
        log_packet = pb.FreeStatus()
        log_packet.RemainTimes = packet.Freespin.RemainTimes
        return log_packet
    return None

def log_piggy_theme(packet):
    log_packet = pb.ThemeStatus()

    log_packet.piggyBank.CurType = packet.piggyBank.CurType
    log_packet.piggyBank.Progress = packet.piggyBank.Progress
    log_packet.piggyBank.BetLimit = packet.piggyBank.BetLimit
    log_packet.piggyBank.AverageBets = packet.piggyBank.AverageBets
    print(log_packet)
    
def log_bingomoo_theme(packet):
    log_packet = pb.ThemeStatus()

    log_packet.bingoMoo.Data.CurType = packet.bingoMoo.Data.CurType
    log_packet.bingoMoo.Data.AverageBets = packet.bingoMoo.Data.AverageBets
    log_packet.bingoMoo.Data.Progress = packet.bingoMoo.Data.Progress
    # log_packet.bingoMoo.Data.ClearField("FeatureBingoPanel")
    # log_packet.bingoMoo.Data.ClearField("BingoPanelArr")
    
    print(log_packet)
    

def main():
    pass

if __name__ == '__main__':
	main()