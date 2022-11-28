#! /usr/bin/env
#coding=utf-8

import conf
import pressure
import net
import gen.proto as pb

def testTransportor():
    tr = net.Transportor("10.0.84.74:9999")
    req = pb.BunchRequest()
    req.SID = 1
    req.Login.NativeChannel.Name = "yx_01"
    req.Login.NativeChannel.Timezone = "+8"
    tr.send_result(req)
    return

def main():
    theme_id = int(conf.pressure_theme()[0])
    process = conf.pressure_process()
    acc = conf.pressure_acc()
    lv = conf.pressure_level()
    coin = conf.pressure_init_coin()
    spin_times = conf.pressure_spin_times()
    addr = conf.get_svr_url()
    
    player = pressure.PreRobot(addr, acc, theme_id, spin_times)
    player.prepare()
    player.send_cmd("currency coin," + coin)
    player.send_cmd("setlevel " + lv)
    player.run()


if __name__ == '__main__':
	main()
