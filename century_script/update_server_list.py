#! /usr/bin/env
#coding=utf-8

import yaml

conf_file = '~/jenkins/server_config.yaml'

def main():
	with open(conf_file) as f:
		data = yaml.load(f, Loader=yaml.FullLoader)
		print(data)

if __name__ == '__main__':
	main()
