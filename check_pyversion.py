#!/bin/bash/python

import sys
import re
import os

def check_py():
	py_v = sys.version[0:3]
	if (py_v == '2.7'):
		print('current python version is 2.7')
	else:
		versions = os.popen('sudo update-alternatives --list python','r')
		versions = (versions.read()).split('\n')
		versions.pop()
		#print(versions)
		vs_list = []
		for vs in versions:
			vs_list.append((re.findall(r'/usr/bin/python(.*$)',vs))[0])
		if '2.7' in vs_list:
			py_v2 = sys.version[0:3]
			os.system('sudo ln -s -f /usr/bin/python2.7 /usr/bin/python')
		else:
			print('NO PYTHON 2.7 IN SYSTEM\nSTART INSTALL PYTHON 2.7')
			os.system('sudo apt-get install python2.7')
			os.system('sudo apt update')
			os.system('sudo apt install python-pip')
			os.system('pip install --upgrade pip')
			os.system('sudo ln -s -f /usr/bin/python2.7 /usr/bin/python')
			print('INSTALLING DONE')

check_py()
