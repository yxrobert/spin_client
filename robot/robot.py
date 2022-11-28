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
add_money = "add coin 99999999999"


def log_output(name, content):
    file_name = log_name.format(name)
    with open(file_name, "ab+") as f:
        print >> f, content

class RobotBase:
    def __init__(self, name):
        self.name = name
        self.err_count = 0
        self.err_max = 3
        self.log_switch = True

    def log(self, *content):
        print(content)
        if self.log_switch:
            log_output(self.name, content)
         
    def log_err(self, *content):
        print(content)
        log_output(self.name, content)
    
    # def log_output(name, content):
    #     file_name = log_name.formati(name)
    #     with open(file_name, "a+") as f:
    #         print >> f, content

    def send_packet(self, req):
        if self.err_count >= self.err_max:
            self.log_err("err max")
            exit(1)

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

    def req_novice_save(self, _id):
        self.log("req_novice")
        req = make_novice_save_req(self.player_id, self.token, _id)
        self.send_packet(req)

    def req_play(self, theme_id, bet, pick_id, pick_ids):
        self.log("req_play", bet)
        req = make_play_req(self.player_id, self.token, theme_id, bet, pick_id, pick_ids)
        self.send_packet(req)

    def req_pick(self, theme_id, bet, x, y):
        self.log("req_pick")
        req = make_pick_req(self.player_id, self.token, theme_id, bet, x, y)
        self.send_packet(req)

    def req_game(self, theme_id, bet, x, y):
        self.log("req_game")
        req = make_game_req(self.player_id, self.token, theme_id, bet, x, y)
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

    def req_activity_user_data(self, uid):
        req = make_activity_user_data_req(self.player_id, self.token, uid)
        self.send_packet(req)  

    def req_activity_play(self, uid):
        req = make_activity_play_req(self.player_id, self.token, uid)
        self.send_packet(req)

    def req_cardgathering_data(self, season):
        req = make_cardgathering_data_req(self.player_id, self.token, season)
        self.send_packet(req)

    def req_cardgathering_exchange(self, src, dest):
        req = make_cardgathering_exchange_req(self.player_id, self.token, src, dest)
        self.send_packet(req)

    def req_cardgathering_break(self, level, card_list):
        req = make_cardgathering_break_req(self.player_id, self.token, level, card_list)
        self.send_packet(req)

    def req_cardgathering_reset(self):
        req = make_cardgathering_reset_req(self.player_id, self.token)
        self.send_packet(req)

    def req_cardgathering_gameaward(self):
        req = make_cardgathering_gameaward_req(self.player_id, self.token)
        self.send_packet(req)

    def req_levelsprint_get(self):
        req = make_levelsprint_get_req(self.player_id, self.token)
        self.send_packet(req)

    def req_levelsprint_draw(self):
        req = make_levelsprint_draw_req(self.player_id, self.token)
        self.send_packet(req)

    def req_hero_active(self, id, name):
        req = make_hero_active_req(self.player_id, self.token, id, name)
        self.send_packet(req)

    def req_treasure_get(self):
        req = make_treasure_get_req(self.player_id, self.token)
        self.send_packet(req)

    def req_bonus(self, src, act):
        req = make_bonus_req(self.player_id, self.token, src, act)
        self.send_packet(req)

    def on_response(self, packet):
        if packet.Error != None:
            # self.log("--------Got Error--------[" + str(packet.Error) + "]")
            self.process_err(packet.Error)

        if packet.HasField("Login"):
            self.on_login(packet)
            return

        for r in packet.Multi.Responses:
            if r.HasField("ThemeStatus"):
                self.on_theme_status(r.ThemeStatus)
            elif r.HasField("Play"):
                self.on_play(r.Play)
            elif r.HasField("Activity"):
                self.on_activity(r.Activity)
            elif r.HasField("CardGathering"):
                self.on_cardgathering(r.CardGathering)
            # elif packet.HasField("TreasureRoom"):
            #     self.on_treasure(packet.TreasureRoom)
            elif r.HasField("LevelSprint"):
                self.on_levelsprint(r.LevelSprint)
                pass
        
        self.log("Awards", packet.Multi.Awards)
        self.log("ActivityEventDropList", packet.Multi.ActivityEventDropList)

    def check_relogin(self, err_str):
        print(err_str)
        return err_str.find("token-match") > 0 or err_str.find("bad-auth") > 0 or err_str.find("time back") > 0 or err_str.find("need login") > 0

    def process_err(self, err):
        err_str = str(err)
        self.log_err(err_str)
        if self.check_relogin(err_str):
            self.req_login()
        elif err_str.find("not-enough") > 0:
            self.send_cmd(add_money)

    def on_login(self, packet):
        login = packet.Login
        self.set_user_data(login.PlayerID, login.Token)
        save_user_data(self.token, self.player_id)
        # self.log("on_login", login.PlayerID)
        self.print_user_data()     

    def set_user_data(self, user_id, token):
        self.player_id = int(user_id)
        self.token = token

    def print_user_data(self):
        self.log("[name:%s uid:%d token:%s]" % (self.name, self.player_id, self.token))

    def on_play(self, packet):
        pass

    def on_theme_status(self, packet):
        pass

    def on_activity(self, packet):
        if packet.HasField("List"):
            self.log(packet.List)
        elif packet.HasField("UserData"):
            self.on_act_userdata(packet.UserData)
        elif packet.HasField("Play"):
            self.on_act_play(packet.Play)
        pass

    def on_act_play(self, packet):
        self.log(packet)

    def on_act_userdata(self, packet):
        self.log(packet)

    def on_cardgathering(self, packet):
        self.log(packet)

    def on_levelsprint(self, packet):
        self.log(packet)

    def on_treasure(self, packet):
        self.log(packet)


    
class SpinRobot(RobotBase):
    def __init__(self, name, theme_id):
        RobotBase.__init__(self, name)
    
        self.themeData = ThemeData()
        self.theme_id = theme_id
        self.interval = 0.2

    def get_next_stage(self):
        return self.themeData.NextStage

    def set_auto_interval(self, val):
        self.interval = val

    # def set_spin_func(self, f):
    #     self.spin_callback = f

    # def set_theme_func(self, f):
    #     self.theme_callback = f

    def spin(self, pick_id=0, pick_ids=None):
        self.req_play(self.theme_id, self.themeData.get_play_bet(), pick_id, pick_ids)

    def pick(self, x=-1, y=-1):
        self.req_pick(self.theme_id, self.themeData.get_play_bet(), x, y)

    def game(self, x=-1, y=-1):
        self.req_game(self.theme_id, self.themeData.get_play_bet(), x, y)
    
    def serials_game(self, arr):
        print(arr)
        for i in range(0, len(arr)):
            self.req_game(self.theme_id, self.themeData.get_play_bet(), arr[i], -1)
    
    def enter_theme(self):
        self.req_theme_status(self.theme_id)

    def select_bet(self, bet):
        self.themeData.set_play_bet(bet)

    def select_mini_bet(self):
        bet = self.themeData.status.Bets[0]
        self.themeData.set_play_bet(bet)

    def select_max_bet(self):
        bet = self.themeData.status.Bets[-1]
        self.themeData.set_play_bet(bet)

    def select_rand_bet(self):
        bet = self.themeData.status.Bets[random.randint(0,len(self.themeData.status.Bets))]
        # self.log(self.themeData.status.Bets)
        # self.log("rand bet", bet)
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

    def log_spin_wins(self, spin_packet):
        self.log(msg.log_wins(spin_packet))
    
    # stage
    def in_base(self):
        return self.themeData.NextStage == pb.Slot.Stage.BASE

    def in_pick(self):
        return self.themeData.NextStage == pb.Slot.Stage.PICKER

    def in_head_pick(self):
        return self.themeData.NextStage == pb.Slot.Stage.PICKER and self.themeData.CurrentStage != pb.Slot.Stage.PICKER


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