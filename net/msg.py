#! /usr/bin/env
#coding=utf-8

import gen.proto as pb
import random, sys
from sys import maxint

reload(sys)
sys.setdefaultencoding('utf8')

def check_relogin(err_str):
    print(err_str)
    return err_str.find("token-match") > 0 or err_str.find("bad-auth") > 0 or err_str.find("time back") > 0 or err_str.find("need login") > 0

def gen_sid():
    return random.randint(0, maxint/10000000000)
    
def mak_regist_req(name):
    req = pb.BunchRequest()
    req.SID = gen_sid()
    req.Login.NativeChannel.Name = name
    req.Login.NativeChannel.Timezone = "+8"
    return req

def make_login_req(name):
    req = pb.BunchRequest()
    req.SID = gen_sid()
    req.Login.NativeChannel.Name = name
    req.Login.NativeChannel.Timezone = "+8"
    return req

def make_multi_req(player_id, token):
    req = pb.BunchRequest()
    req.SID = gen_sid()
    req.Multi.Auth.PlayerID = player_id
    req.Multi.Auth.Token = token
    request = req.Multi.Requests.add()
    request.RequestID = 0
    request.Step = 34
    return req, request

def make_novice_req(player_id, token):
    req, request = make_multi_req(player_id, token)
    request.NoviceGuide.Holder = False
    return req

def make_novice_save_req(player_id, token, _id):
    req, request = make_multi_req(player_id, token)
    request.NoviceGuideSave.Data.ID = _id
    request.NoviceGuideSave.Data.State = 1
    return req

def make_play_req(player_id, token, theme_id, bet):
    req, request = make_multi_req(player_id, token)

    request.Play.Operation = pb.PlayRequest.OperationType.SPIN
    request.Play.ThemeID = theme_id
    request.Play.TotalBet = bet
    request.Play.PickID = 0
    # request.Play.PickIDs = ""
    request.Play.PickPos = 0
    request.Play.PickInfo = ""

    return req

def make_pick_req(player_id, token, theme_id, bet, x, y = -1):
    req, request = make_multi_req(player_id, token)

    request.Play.Operation = pb.PlayRequest.OperationType.PICK
    request.Play.ThemeID = theme_id
    request.Play.TotalBet = bet
    request.Play.PickID = x
    request.Play.PickPos = 0
    request.Play.PickInfo = ""

    if y != -1:
        request.Play.coords.X = x
        request.Play.coords.y = y
    else:
        request.Play.index.X = x

    return req

def make_game_req(player_id, token, theme_id, bet, x, y = -1):
    req, request = make_multi_req(player_id, token)

    request.Play.Operation = pb.PlayRequest.OperationType.GAME
    request.Play.ThemeID = theme_id
    request.Play.TotalBet = bet
    request.Play.PickID = x
    request.Play.PickPos = 0
    request.Play.PickInfo = ""

    request.Play.index.X = x

    return req

def make_multi_rsp(data):
    rsp = pb.BunchResponse()

    try:
        rsp.ParseFromString(data.strip())
    # except pb._DecodeError :
    except :
        print(str(data))
        # rsp.Error.Msg = str(data).encode(encoding="UTF-8")
        if check_relogin(str(data)):
            rsp.Error.Msg = "need login" 

    return rsp

def make_theme_status_req(player_id, token, theme_id):
    req = pb.BunchRequest()
    req.SID = gen_sid()

    req.Multi.Auth.PlayerID = player_id
    req.Multi.Auth.Token = token

    request = req.Multi.Requests.add()
    request.RequestID = 0
    request.Step = 112

    request.ThemeStatus.ThemeID = theme_id
    return req

def make_debug_req(user_id, theme_id, cmd, bet):
    req = pb.DebugRequest()
    req.GMCommand.UserID = user_id
    req.GMCommand.ThemeID = theme_id
    req.GMCommand.Command = cmd
    req.GMCommand.TotalBet = bet
    return req

def make_debug_cmd_req(user_id, theme_id, cmd, bet):
    req = pb.DebugRequest()
    req.Command.UserID = user_id
    req.Command.ThemeID = theme_id
    req.Command.Command = cmd
    req.Command.TotalBet = bet
    return req

def make_activity_list_req(player_id, token):
    req, request = make_multi_req(player_id, token)
    request.Activity.List.Type = 1
    return req

def make_activity_user_data_req(player_id, token, uid):
    req, request = make_multi_req(player_id, token)
    request.Activity.UserData.UID = uid
    return req

def make_activity_play_req(player_id, token, uid):
    req, request = make_multi_req(player_id, token)
    request.Activity.Play.UID = uid
    request.Activity.Play.Input.InputX = 0
    return req


def make_cardgathering_data_req(player_id, token, season):
    req, request = make_multi_req(player_id, token)
    request.CardGathering.UserData.Season = season
    return req


def make_cardgathering_exchange_req(player_id, token, src, dest):
    req, request = make_multi_req(player_id, token)
    request.CardGathering.ExchangeCard.Src = src
    request.CardGathering.ExchangeCard.Dest = dest
    return req


def make_cardgathering_break_req(player_id, token, level, card_list):
    req, request = make_multi_req(player_id, token)
    request.CardGathering.BreakCard.Level = level
    # request.CardGathering.BreakCard.CostCards.extend(card_list)    
    for c in card_list:
        card = request.CardGathering.BreakCard.CostCards.add()
        card.Entry = c
        card.Num = 1
    return req


def make_cardgathering_reset_req(player_id, token):
    req, request = make_multi_req(player_id, token)
    request.CardGathering.ResetBreaking.Type = 0
    return req

def make_cardgathering_gameaward_req(player_id, token):
    req, request = make_multi_req(player_id, token)
    request.CardGathering.GameAwards.Type = 0
    return req


def make_levelsprint_get_req(player_id, token):
    req, request = make_multi_req(player_id, token)
    request.LevelSprint.Get.Type = 0
    return req

def make_levelsprint_draw_req(player_id, token):
    req, request = make_multi_req(player_id, token)
    request.LevelSprint.DrawLottery.Type = 0
    return req

def make_bonus_req(player_id, token, src, act):
    req, request = make_multi_req(player_id, token)
    request.Bonus.Source = src
    request.Bonus.Action = act
    return req







def main():
    req = make_play_req()
    print(req)


if __name__ == '__main__':
	main()