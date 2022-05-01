#!/bin/sh
sudo apt install wget curl git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison dwarves kernel-package python3 python3-dev python3-pip -y
sudo pip3 install bs4

curl https://linuxcompile.frank-ruan.com/main.py | sudo python3
