#! /usr/bin/env
#coding=utf-8

import time
import conf
import pressure
import net
import gen.proto as pb
from multiprocessing import Process

def testTransportor():
    tr = net.Transportor("10.0.84.74:9999")
    req = pb.BunchRequest()
    req.SID = 1
    req.Login.NativeChannel.Name = "yx_01"
    req.Login.NativeChannel.Timezone = "+8"
    tr.send_result(req)
    return

def main():
    start_time = int(time.time())
    theme_id = int(conf.pressure_theme()[0])
    process = int(conf.pressure_process())
    acc = conf.pressure_acc()
    lv = conf.pressure_level()
    coin = conf.pressure_init_coin()
    spin_times = conf.pressure_spin_times()
    addr = conf.get_svr_url()

    process_list = []
    for i in range(process):
        name = acc + str(i)
        player = pressure.PreRobot(addr, name, theme_id, spin_times)
        p = Process(target=process_run,args=(player, coin, lv))
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()

    cost = (int(time.time()) - start_time)
    print("player[%d] * quest[%d] time [%d(sec)]" % (int(process), int(spin_times), int(cost)))

def process_run(player, coin, lv):
    player.prepare()
    player.send_cmd("currency coin," + coin)
    player.send_cmd("level " + lv)
    player.run()

if __name__ == '__main__':
	main()
