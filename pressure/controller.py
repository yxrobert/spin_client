#! /usr/bin/env
#coding=utf-8

from tiki import *

theme_register = {
    10290 : ThemeController,
}

def create_theme_controller(theme_id):
    if theme_register.has_key(theme_id):
         return theme_register[theme_id](theme_id)   
    else:
        return ThemeController(theme_id)

class ThemeController:
    def __init__(self, theme_id):
        self.theme_id = theme_id

    def do_play(self, robot):
        robot.spin()

    def handle_play(self):
        pass

