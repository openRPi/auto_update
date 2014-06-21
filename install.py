# -*- coding:utf-8 -*-

import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

install_list = ["ipython","mplayer","fbi","vim","git","python-dev","python-pip","tree","lrzsz"]
python_module_list = ["RPIO", "tornado"]
auto_probe_list = ["spi-bcm2708", "i2c-bcm2708", "ads7846"]

def local(name):
	return os.path.join(THIS_DIR, name)

def err_exit(cmd, *args):
	if os.system(" ".join([cmd]+list(args))):
		exit()

def update_app():
	print "@ 更新软件源..."
	err_exit("apt-get update")

	for name in install_list:
		print "@ 安装 %s ..." %(name,)
		err_exit("apt-get install -y",name)

	for name in python_module_list:
		print "@ 安装 %s ..." %(name,)
		err_exit("pip install",name)

	print "@ 安装 ngrok ..."
	err_exit("install", local("app/ngrok"), "/usr/local/bin")

	print "@ 安装 fbcp ..."
	err_exit("install", local("app/fbcp"), "/usr/local/bin")

def update_kernel_modules():
	print "@ 安装新内核..."
	err_exit("cp -rf", local("kernel/kernel.img"), "/boot")
	print "@ 安装新模块..."
	err_exit("cp -rf", local("kernel/lib"), "/")

def update_server():
	print "@ 安装 mutt ..."
	err_exit("apt-get install mutt")
	err_exit("cp -rf", local("mutt/Muttrc"), "/etc")

	print "@ 安装 msmtp ..."
	err_exit("apt-get install msmtp")
	err_exit("cp -rf", local("msmtp/msmtprc"), "/etc")

def update_modprobe():
	print "@ 取消 modprobe 黑名单"
	err_exit("mv /etc/modprobe.d/raspi-blacklist.conf /etc/modprobe.d/raspi-blacklist.conf.bak")

	for name in auto_probe_list:
		print "@ 设置开机自加载 %s ..." %(name,)
		err_exit("echo", name, ">>", "/etc/modules")

if __name__ == '__main__':
	update_app()
	update_server()
	update_modprobe()
	update_kernel_modules()
	print "已结束"