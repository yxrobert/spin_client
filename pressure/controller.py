#! /usr/bin/env
#coding=utf-8

class ThemeController:
    def __init__(self, theme_id):
        self.theme_id = theme_id

    def do_play(self, robot):
        robot.spin()

    def handle_play(self, packet):
        pass

    def handle_theme_status(self, packet):
        pass
