#! /usr/bin/env
#coding=utf-8

from controller import ThemeController

class Genie(ThemeController):
    def __init__(self, theme_id):
        ThemeController.__init__(self, theme_id)

    def do_play(self, robot):
        if robot.in_pick():
            robot.pick(x=0)
            return
        
        robot.spin()

    def handle_play(self):
        pass