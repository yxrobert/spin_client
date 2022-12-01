#! /usr/bin/env
#coding=utf-8

from random import randint
from controller import ThemeController

class Witch(ThemeController):
    def __init__(self, theme_id):
        ThemeController.__init__(self, theme_id)

    def do_play(self, robot):
        if robot.in_pick():
            robot.pick(x=randint(1,4))
            return
        
        robot.spin()

    def handle_play(self, packet):
        pass