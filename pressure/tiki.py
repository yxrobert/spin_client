#! /usr/bin/env
#coding=utf-8

from pressure import ThemeController

class Tiki(ThemeController):
    def __init__(self, theme_id):
        ThemeController.__init__(self, theme_id)

    def do_play(self, robot):
        if robot.in_head_pick():
            # robot.spin()
            self.pick_id = 0

        if robot.in_pick():
            robot.spin(pick_id=self.pick_id)
            self.pick_id += 1
            return
        
        robot.spin()

    def handle_play(self):
        pass