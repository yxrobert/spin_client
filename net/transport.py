#! /usr/bin/env
#coding=utf-8

import time
import httplib
import gen.proto as pb
from msg import *


class Transportor:
    server_addr = "127.0.0.1:9999"
    server_gateway_url = "/gateway"
    server_debug_url = "/debug"
    server_time_fake2 = "/timeFake2"
    header = {'user-agent':'BestHTTP/2 v2.5.2'}
    interval = 0.2
    g_ssid = 0

    def __init__(self, addr):
        self.server_addr = addr

    def gen_header(self):
        hm = self.header
        hm['SessionID'] = gen_sid()
        self.g_ssid += 1
        hm['SID'] = self.g_ssid
        return hm

    def set_server_addr(self, server_addr):
        self.server_addr = server_addr

    def send(self, packet, server_url):
        data = packet.SerializeToString()
        conn = httplib.HTTPConnection(self.server_addr)
        conn.request('POST', server_url, data, self.gen_header())
        return conn.getresponse()

    def send_debug(self, packet):
        data = packet.SerializeToString()
        conn = httplib.HTTPConnection(self.server_addr)
        conn.request('POST', self.server_debug_url, data, self.gen_header())
        return conn.getresponse()

    def send_debug_result(self, packet):
        response = self.send_debug(packet, self.server_gateway_url)
        print(response.status)
        print(response.read())

    def send_result(self, packet):
        response = self.send(packet, self.server_gateway_url)
        print(response.status)
        time.sleep(self.interval)

        data = response.read()
        rsp = make_multi_rsp(data)
        return rsp

    def send_timefake(self, data):
        conn = httplib.HTTPConnection(self.server_addr)
        conn.request('POST', self.server_time_fake2, data, self.gen_header())
        return conn.getresponse()

def main():
    tr = Transportor("127.0.0.1:9999")
    req = pb.BunchRequest()
    req.SID = 1
    req.Login.NativeChannel.Name = "yx_01"
    req.Login.NativeChannel.Timezone = "+8"
    tr.send_result(req)
    pass

if __name__ == '__main__':
	main()