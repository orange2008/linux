#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


html = urlopen("https://kernel.org")
bs = BeautifulSoup(html, "html.parser")
xzlink = bs.find(id='latest_link')
xz = xzlink.a['href']
os.mkdir("linuxkrnl")
os.chdir("linuxkrnl")
os.system("wget --no-check-certificate " + xz)
os.system("tar -xvf *.tar.xz")
xzname = os.listdir()[0]
ver = xzname.replace("linux-", "").replace(".tar.xz", "")
os.chdir(xzname.replace(".tar.xz", ""))
f = open("Makefile", "r+")
flist = f.readlines()
if "EXTRAVERSION" in flist[4]:
    flist[4] = "EXTRAVERSION = -orwtmc\n"
else:
    print("Please change the Makefile by yourself")
    pause = input("Press any key to continue...")

if "NAME" in flist[5]:
    flist[5] = "NAME = ORWTMC Kernel\n"
else:
    print("Please change the Makefile by yourself")
    pause = input("Press any key to continue...")

f.close()

f = open("Makefile", 'w+')
f.writelines(flist)
f.close()
os.system("make mrproper")
os.system("make clean")
print("\n\n\n")
print("Now exiting the script. Please run 'make menuconfig' by yourself")
print("Run 'curl https://linuxcompile.frank-ruan.com/continue.py | sudo python3' to continue")
print("\n\n\n\n\n")
