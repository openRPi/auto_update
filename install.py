# -*- coding:utf-8 -*-

import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

install_list = ["ipython","mplayer","fbi","vim","git","python-dev","python-pip","tree","lrzsz"]
python_module_list = ["RPIO", "tornado"]

print "@ 更新软件源..."
if os.system("apt-get update"):
	exit()

for name in install_list:
	print "@ 安装 %s ..." %(name,)
	if os.system("apt-get install %s" %(name,)):
		exit()

for name in python_module_list:
	print "@ 安装 %s ..." %(name,)
	if os.system("pip install %s" %(name,)):
		exit()

print "@ 安装 ngrok ..."
if os.system("install ngrok /usr/local/bin"):
	exit()

print "@ 安装 fbpc ..."
if os.system("install fbpc /usr/local/bin"):
	exit()
