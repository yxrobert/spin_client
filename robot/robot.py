#! /usr/bin/env
#coding=utf-8

from struct import pack
import time
from net import *
import gen.proto as pb
from theme_data import ThemeData
import msg
from conf import save_user_data, get_user_id, get_token

log_name = "./log/{}.log"

class RobotBase:
    def __init__(self, name):
        self.name = name

    def log(self, *content):
        print(content)
        file_name = log_name.format(self.name)
        # with open(file_name, "w+") as f:
        #     lines = f.readlines()
        #     for c in content:
        #         lines.append(str(c))
        #     f.seek(0)
        #     f.writelines(lines)
        with open(file_name, "a+") as f:
            print >> f, content

    def send_packet(self, req):
        rsp = Sender.send_result(req)
        self.on_response(rsp)

    def req_login(self):
        self.log("req_login")
        req = make_login_req(self.name)
        self.send_packet(req)

    def req_novice(self):
        self.log("req_novice")
        req = make_novice_req(self.player_id, self.token)
        self.send_packet(req)

    def req_novice_save(self):
        self.log("req_novice")
        req = make_novice_save_req(self.player_id, self.token)
        self.send_packet(req)

    def req_play(self, theme_id, bet):
        self.log("req_play", bet)
        req = make_play_req(self.player_id, self.token, theme_id, bet)
        self.send_packet(req)

    def req_pick(self, theme_id, bet, x, y):
        self.log("req_pick")
        req = make_pick_req(self.player_id, self.token, theme_id, bet, x, y)
        self.send_packet(req)

    def req_theme_status(self, theme_id):
        self.log("req_theme_status")
        req = make_theme_status_req(self.player_id, self.token, theme_id)
        self.send_packet(req)

    def req_debug(self, player_id, theme_id, cmd, bet):
        self.log("req_debug : ", cmd)
        req = make_debug_req(player_id, theme_id, cmd, bet)
        Sender.send_debug(req)

    def on_debug_response(self, packet):
        self.log(packet)

    def req_debug_cmd(self, player_id, theme_id, cmd, bet):
        self.log("req_debug : ", cmd)
        req = make_debug_cmd_req(player_id, theme_id, cmd, bet)
        Sender.send_debug(req)

    def req_activity_list(self):
        req = make_activity_list_req(self.player_id, self.token)
        self.send_packet(req)

    def req_activity_list(self):
        req = make_activity_list_req(self.player_id, self.token)
        self.send_packet(req)  

    def req_activity_user_data(self):
        req = make_activity_user_data_req(self.player_id, self.token)
        self.send_packet(req)  

    def req_activity_play(self):
        req = make_activity_play_req(self.player_id, self.token)
        self.send_packet(req)  

    def on_response(self, packet):
        if packet.Error != None:
            self.log(packet.Error)
            self.process_err(packet.Error)

        if packet.HasField("Login"):
            self.on_login(packet)
            return

        for r in packet.Multi.Responses:
            if r.HasField("ThemeStatus"):
                self.on_theme_status(r.ThemeStatus)
            elif r.HasField("Play"):
                self.on_play(r.Play)
    
    def process_err(self, err):
        if str(err).find("token-match") > 0:
            self.req_login()

    def on_login(self, packet):
        login = packet.Login
        self.set_user_data(login.PlayerID, login.Token)
        save_user_data(self.token, self.player_id)
        self.log("on_login", login.PlayerID)        

    def set_user_data(self, user_id, token):
        self.player_id = int(user_id)
        self.token = token

    def on_play(self, packet):
        pass

    def on_theme_status(self, packet):
        pass


    
class SpinRobot(RobotBase):
    def __init__(self, name, theme_id):
        RobotBase.__init__(self, name)
    
        self.themeData = ThemeData()
        self.theme_id = theme_id
        self.interval = 0.2

    def set_auto_interval(self, val):
        self.interval = val

    # def set_spin_func(self, f):
    #     self.spin_callback = f

    # def set_theme_func(self, f):
    #     self.theme_callback = f

    def spin(self):
        self.req_play(self.theme_id, self.themeData.get_play_bet())

    def pick(self, x=-1, y=-1):
        self.req_pick(self.theme_id, self.themeData.get_play_bet(), x, y)
    
    def enter_theme(self):
        self.req_theme_status(self.theme_id)

    def select_bet(self, bet):
        self.themeData.set_play_bet(bet)

    def on_theme_status(self, packet):
        self.themeData.update_from_theme(packet)
        self.log("on_theme_status")
        self.log(msg.log_theme_status(packet))
        self.theme_status_callback(packet)

    def on_play(self, packet):
        self.themeData.update_from_play(packet)
        self.log("on_play")
        self.themeData.show_stage()
        self.play_status_callback(packet)
    
    def theme_status_callback(self, packet):
        pass

    def play_status_callback(self, packet):
        pass

    def spin_to_base(self):
        self.spin()
        while self.themeData.get_stage() != pb.Slot.Stage.BASE:
            self.spin()
            time.sleep(self.interval)

    def spin_times(self, times):
        for i in range(0, times):
            self.spin()

    def spin_to_next_stage(self):
        cur_stage = self.themeData.get_stage()
        self.spin_left_stage(cur_stage) 

    def spin_left_stage(self, stage):
        while self.themeData.get_stage() == stage:
            self.spin()
            time.sleep(self.interval)

    def send_gm(self, cmd):
        RobotBase.req_debug(self, self.player_id, self.theme_id, cmd,
         self.themeData.get_play_bet())

    def send_cmd(self, cmd):
        RobotBase.req_debug_cmd(self, self.player_id, self.theme_id, cmd,
         self.themeData.get_play_bet())

    def gm_clear(self):
        self.send_gm("clear")



def robot_init(robot):
    robot.set_user_data(get_user_id(), get_token())
    # r.req_login()

    robot.enter_theme()
    return robot

def main():
    robot = SpinRobot(1152939921426612225, "070360ce-3eff-4c89-8cb1-9fbb3a8981f3", 10070)
    robot.spin()

if __name__ == '__main__':
	main()