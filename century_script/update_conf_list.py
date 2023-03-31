#! /usr/bin/env
#coding=utf-8

import os, sys, subprocess
import yaml

#conf_file = '/root/jenkins/server_config.yaml'
config_file = './config.list'
conf_dir = '/home/user00/jenkins/cc-conf'

def cmd_list(path):
	return 'protokitgo drive list --config=' + path + '/setting.yaml --log_level=0 --log_color=false'

def find_flag(l):
	return l.find("===================") >= 0

def parse_line(l):
	dl = l.strip().split(" ")
	return dl

def parse_data(s):
	b_in = False
	data_list = []	
	
	for l in s.split("\n"):
		if b_in:
			if not find_flag(l):
				dl = parse_line(l)
				if len(dl) > 0:
					data_list.append(dl)

		if find_flag(l):
			b_in = not b_in
			
		#print(l)

	return sorted(data_list)
	pass

def main():
	os.system('cd ' + conf_dir)

	ret = subprocess.check_output(cmd_list(conf_dir), shell=True)
	output = parse_data(ret)
	#print(output)


	desc = "CLDesc="
	name = "CL="
	
	for d in output:
		name += "%s," % (d[0])
		desc += "%s," % (d[0])

	with open(config_file, 'w') as ff:
		ff.write(name[:-2])
		ff.write("\n")
		ff.write(desc[:-2])
		print(name[:-1])
		print(desc[:-1])

if __name__ == '__main__':
	main()
