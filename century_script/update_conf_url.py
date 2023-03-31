#! /usr/bin/env
# -*- coding: utf-8 -*-

import os, sys, subprocess, time
import yaml
from update_conf_list import *

reload(sys)
sys.setdefaultencoding("utf-8")

url_file="conf_url.txt"

def parse_url_data(s):
	b_in = False
	data_list = []	
	
	for l in s.split("\n"):
		if b_in:
			if not find_flag(l):
				dl = parse_url_line(l)
				if len(dl) > 0:
					data_list.append(dl)

		if find_flag(l):
			b_in = not b_in
			
		#print(l)

	return data_list

def parse_url_line(l):
	dl = parse_line(l)
	rl = []
	for s in dl:
		if s != "":
			rl.append(s)
			if len(rl) >= 2:
				break
	return rl

url_head = "<li>\n"
url_tail = "</li>\n"
url_fmt = '<a href="https://docs.google.com/spreadsheets/d/%s/edit#gid=0">%s</a>\n'

def gen_group_xml(l):
	print(l)
	s = ""
	for i in l:
		s += url_fmt % (i[1], i[0])
	return s	

def gen_xml(l):
	m = {}
	for i in l:
		k = i[0][0]
		if k == '':
			continue
		if m.has_key(k):
			m[k].append(i)
		else:
			m[k] = [i]		
	
	n = 0
	s = ''
	for i in sorted(m):
		if n == 0:
			s += url_head
		n += len(m[i])	
		s += gen_group_xml(m[i])	
		if n >= 1:
			n = 0
			s += url_tail

	return s

jobs_dir = "jobs/"
suffix = ".xml"
jk_dir = "/var/lib/docker/volumes/jenkins-data/_data"

def update_jobs(s):
	os.system('cd ' + jk_dir)
	for parent, dirnames, filenames in os.walk(jobs_dir):
		for filename in filenames:
			if filename.find(suffix) != -1 and filename.find('back') == -1:
				f_name = os.path.join(parent, filename)
				if f_name.find('build') != -1:
					continue
				#print(f_name)
				update_jobs_xml(f_name, s)
	pass

desc_head = "<description>"
desc_tail = "</description>"
li_head = "&lt;li&gt;"
li_tail = "&lt;/li&gt;"
tar_str = li_tail + desc_tail

def check_head(l):
	idx = l.find(desc_head)	
	if idx >= 0:
		pos = idx + len(desc_head)
		s = l[pos : pos + len(li_head)]
		#print(s)
		#if s != li_head:
		#	idx = -1
	return idx	

def check_tail(l):
	idx = l.find(desc_tail)
	if idx >= 0:
		pos = idx - len(li_tail)
		s = l[pos : idx]
		#print(s)
		if s != li_tail:
			idx = -1
	return idx

def update_jobs_xml(f_name, s):
	lines, head, tail = check_jobs_content(f_name)
	print(f_name)
	print(head, tail)
	if head != -1 and tail != -1:
		backup_xml(f_name, lines)
		new_xml(f_name, lines, s, head, tail)
		exit(0)

def new_xml(f_name, lines, s, head, tail):
	print(f_name)
	with open(f_name, 'w+') as f:
		head = head + 1
		tail = tail - 1
		for i in range(len(lines)):
			if i >= head and i <= tail:
				if i == head:
					f.write(s)
				continue
			else:
				f.write(lines[i])			
	
def backup_xml(f_name, lines):
	backup = f_name + time.strftime(".%Y%m%d", time.localtime())+ ".backup"
	try:
		with open(backup, 'x') as f:
			for l in lines:
				f.write(l)
		print(backup)
	except:
		pass

def check_jobs_content(f_name):
	lines = []
	head = -1
	tail = -1
	with open(f_name) as f:
		lines = f.readlines()
		for i in range(0, len(lines)):
			l = lines[i]
			if head == -1:
				h = check_head(l)
				if h != -1 and lines[i + 1].find(li_head) != -1:
					head = i
					continue
			
			if tail == -1:
				t = check_tail(l)
				if t != -1:
					tail = i
					continue
		
		if head != -1 and tail != -1:
			print("%s : (%d %d)" % (f_name, head, tail))
	return lines, head, tail

def main():
	os.system('cd ' + conf_dir)

	ret = subprocess.check_output(cmd_list(conf_dir), shell=True)
	output = parse_url_data(ret)
	#print(output)
	#print(len(output))
	s = gen_xml(output)
	print(s)

	with open(url_file, 'w') as ff:
		ff.write(s)

	#update_jobs(s)

if __name__ == '__main__':
	main()
