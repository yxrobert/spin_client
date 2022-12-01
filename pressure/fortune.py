#! /usr/bin/env
#coding=utf-8

from controller import ThemeController
from random import randint

class Fortune(ThemeController):
    def __init__(self, theme_id):
        ThemeController.__init__(self, theme_id)
        self.game_id = 0

    def do_play(self, robot):
        if robot.in_head_game():
            self.game_id = 0

        # robot.tell_stage()
        if robot.in_game():
            robot.game(x=self.game_id)
        elif robot.in_pick():
            robot.pick(x=randint(0, 1))
        else:
            robot.spin()

    def handle_play(self, packet):
        if packet.HasField("Game"):
            self.game_id = len(packet.Game.fortuneGame.PickList)
        pass

    def handle_theme_status(self, packet):
        if packet.HasField("Gamer"):
            self.game_id = len(packet.Gamer.fortuneGame.PickList)
        pass