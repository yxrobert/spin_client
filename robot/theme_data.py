#! /usr/bin/env
#coding=utf-8

import gen.proto as pb

default_bet = 20000

class ThemeData:
    def __init__(self):
        self.status = pb.ThemeStatus()
        # self.status.Picker = pb.PickerStatus()
        
    def update_from_theme(self, packet):
        self.status = packet

    def update_from_play(self, packet):
        if packet.HasField("Game"):
            self.status.CurrentStage = packet.Game.CurrentStage
            self.status.NextStage = packet.Game.NextStage
        else:
            self.status.CurrentStage = packet.Spin.CurrentStage
            self.status.NextStage = packet.Spin.NextStage
        
        for bet in packet.Spin.UserBets:
            if bet == packet.Spin.TotalBet:
                self.status.LastBet = packet.Spin.TotalBet
                break

    def get_stage(self):
        return self.status.NextStage

    def show_stage(self):
        print("cur_stage : ", self.status.CurrentStage, self.status.NextStage)

    def show_more_stage(self):
        # if self.status.Freespin != None:
            print(self.status.Freespin)

    def set_play_bet(self, bet):
        self.status.LastBet = bet

    def get_play_bet(self):
        if self.status.LastBet <= 0:
            return default_bet

        return self.status.LastBet