#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import Dot11,Dot11Beacon,Dot11Elt,RadioTap,sendp,hexdump
from scapy.all import *

conf.use_pcap = True

netSSID = 'gogogo'       #Network name here
iface = 'wlan0'         #Interface name here

dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33')
beacon = Dot11Beacon(cap='ESS+privacy')
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))
rsn = Dot11Elt(ID='RSNinfo', info=(
'\x01\x00'                 #RSN Version 1
'\x00\x0f\xac\x02'         #Group Cipher Suite : 00-0f-ac TKIP
'\x02\x00'                 #2 Pairwise Cipher Suites (next two lines)
'\x00\x0f\xac\x04'         #AES Cipher
'\x00\x0f\xac\x02'         #TKIP Cipher
'\x01\x00'                 #1 Authentication Key Managment Suite (line below)
'\x00\x0f\xac\x02'         #Pre-Shared Key
'\x00\x00'))               #RSN Capabilities (no extra capabilities)

frame = RadioTap()/dot11/beacon/essid/rsn
# frame =  PrismHeader()/dot11/beacon/essid/rsn
# frame = dot11/beacon/essid/rsn

# frame.show()
# print("\nHexdump of frame:")
# hexdump(frame)
# input("\nPress enter to start\n")

# print(conf.use_pcap)
scapy_cap = rdpcap('magic.pcap')

for pkt in scapy_cap:
    sendp(pkt, iface=iface, loop=1, inter=0.01)


# sendp(frame, iface=iface, loop=1)
