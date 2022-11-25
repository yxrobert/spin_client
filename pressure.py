#! /usr/bin/env
#coding=utf-8

import conf
import pressure

def main():
    theme_id = int(conf.pressure_theme()[0])
    process = conf.pressure_process()
    acc = conf.pressure_acc()
    lv = conf.pressure_level()
    coin = conf.pressure_init_coin()
    spin_times = conf.pressure_spin_times()
    
    player = pressure.PreRobot(acc, theme_id, spin_times)
    player.prepare()
    player.send_cmd("currency coin," + coin)
    player.send_cmd("setlevel " + lv)
    player.run()


if __name__ == '__main__':
	main()