#! /usr/bin/env
#coding=utf-8

import sys
import urllib

def main():
	i = ''
	i = sys.arvg[1]		
	f = urllib.unquote(i).decode('utf8')
	print(f)

if __name__ == '__main__':
	main()
