#!/bin/bash

sudo apt-get install vim
echo '修改hosts配置'
sudo chmod -R 777 /etc/hosts
echo '192.30.255.112  github.com git
185.31.16.184 github.global.ssl.fastly.net'>>/etc/hosts
sudo /etc/init.d/networking restart
echo '检查python版本'
sudo python GL_init/check_pyversion.py
echo '安装必需的python第三方库'
sudo apt-get install python-pip
pip install --upgrade pip
sudo pip install enum
sudo pip install scipy
sudo pip install tensorflow==1.12
sudo apt-get install autoconf automake libtool cmake python-numpy
echo '安装GL.git'
git clone https://github.com/alibaba/graph-learn.git
