#! /usr/bin/env
#coding=utf-8

import time
import httplib

from msg import *


class Sender:
    server_addr = "127.0.0.1:9000"
    server_gateway_url = "/gateway"
    server_debug_url = "/debug"
    server_time_fake2 = "/timeFake2"
    header = {'user-agent':'BestHTTP/2 v2.5.2'}
    interval = 0.2

    @classmethod
    def set_server_addr(cls, server_addr):
        cls.server_addr = server_addr

    @classmethod
    def send(cls, packet, server_url):
        data = packet.SerializeToString()
        conn = httplib.HTTPConnection(cls.server_addr)
        conn.request('POST', server_url, data, cls.header)
        return conn.getresponse()

    @classmethod
    def send_debug(cls, packet):
        data = packet.SerializeToString()
        conn = httplib.HTTPConnection(cls.server_addr)
        conn.request('POST', cls.server_debug_url, data, cls.header)
        return conn.getresponse()

    @classmethod
    def send_debug_result(cls, packet):
        response = cls.send_debug(packet, cls.server_gateway_url)
        print(response.status)
        print(response.read())

    @classmethod
    def send_result(cls, packet):
        response = cls.send(packet, cls.server_gateway_url)
        print(response.status)
        time.sleep(cls.interval)

        data = response.read()
        rsp = make_multi_rsp(data)
        return rsp

    @classmethod
    def send_timefake(cls, data):
        conn = httplib.HTTPConnection(cls.server_addr)
        conn.request('POST', cls.server_time_fake2, data, cls.header)
        return conn.getresponse()

def main():
    pass

if __name__ == '__main__':
	main()