#! /usr/bin/env
#coding=utf-8

import time
import httplib
from requests import Request, Session
import gen.proto as pb
from msg import *


class Requester:
    server_addr = "127.0.0.1:9999"
    server_gateway_url = "/gateway"
    server_debug_url = "/debug"
    server_time_fake2 = "/timeFake2"
    header = {'user-agent':'BestHTTP/2 v2.5.2'}
    interval = 0.2
    g_ssid = 0

    def __init__(self, addr):
        self.server_addr = addr
        self.s = Session()
        # self.conn.headers.update(self.gen_header())

    def gen_header(self):
        hm = self.header
        hm['SessionID'] = str(gen_sid())
        self.g_ssid += 1
        hm['SID'] = str(self.g_ssid)
        return hm

    def set_server_addr(self, server_addr):
        self.server_addr = server_addr

    def gen_addr(self, server_url):
        return "http://" + self.server_addr + server_url

    def send(self, packet, server_url):
        data = packet.SerializeToString()
        req = Request('POST', self.gen_addr(server_url), data=data, headers=self.gen_header())
        prepped = req.prepare()
        return self.s.send(prepped)

    def send_debug(self, packet):
        data = packet.SerializeToString()
        req = Request('POST', self.gen_addr(self.server_debug_url), data=data, headers=self.gen_header())
        prepped = req.prepare()
        return self.s.send(prepped)

    def send_timefake(self, data):
        conn = httplib.HTTPConnection(self.server_addr)
        req = Request('POST', self.gen_addr(self.server_time_fake2), data=data, headers=self.gen_header())
        prepped = req.prepare()
        return self.s.send(prepped)

    def send_debug_result(self, packet):
        response = self.send_debug(packet, self.server_gateway_url)
        print(response.status_code)
        print(response.content)

    def send_result(self, packet):
        response = self.send(packet, self.server_gateway_url)
        if response.status_code != 200:
            print(response.status)
        time.sleep(self.interval)

        data = response.content
        rsp = make_multi_rsp(data)
        return rsp



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