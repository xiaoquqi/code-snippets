#!/bin/bash

sudo raspi-config

sudo pip3 install opencv-contrib-python
sudo apt install libjasper1 libatlas-base-dev
apt install libqtgui4 libqt4-test

# source.list update
sudo sed -i 's|//archive.raspberrypi.org|//mirrors.ustc.edu.cn/archive.raspberrypi.org|g' /etc/apt/sources.list.d/raspi.list
