#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import Dot11,Dot11Beacon,Dot11Elt,RadioTap,sendp,hexdump
from scapy.all import *
import binascii

# conf.use_pcap = True

iface = 'wlan0'         #Interface name here

dot11 = Dot11(type=2, subtype=0, addr1='9c:95:61:72:96:e9', addr2='88:de:a9:cb:e2:fe', addr3='9c:95:61:72:96:e9')
data = "\xff\xff\xff\xff\xff\xff\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9\x9c\x95\x61\x72\x96\xe9"

# data = "\xff\xff"

data = binascii.unhexlify('ffffffffffff9c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e99c95617296e9')

# frame = RadioTap()/dot11/LLC()/data
frame = RadioTap()/dot11/data

# del frame[LLC]

# dot11.show()

frame.show()
# print("\nHexdump of frame:")
# hexdump(frame)
# input("\nPress enter to start\n")

sendp(frame, iface=iface, loop=1, inter=0.2)
