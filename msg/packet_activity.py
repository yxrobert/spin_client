#! /usr/bin/env
#coding=utf-8

import gen.proto as pb

def log_act_bigo(robot, packet):
    if packet.data.HasField("Bingo"):
        log_packet = pb.Bingo.Data()
        log_packet.BingoBall = packet.data.Bingo.BingoBall
        log_packet.StageIdx = packet.data.Bingo.StageIdx
        log_packet.BoardIdx = packet.data.Bingo.BoardIdx
        log_packet.Progress = packet.data.Bingo.Progress
        # log_packet.CurBoard.CurCard = packet.data.Bingo.CurBoard.CurCard
        # robot.log(packet.data.Bingo.CurBoard)
        # robot.log(packet.data.Bingo)
        # robot.log(log_packet)

def log_act_all(robot, packet):
    robot.log(packet)

def main():
    pass

if __name__ == '__main__':
	main()