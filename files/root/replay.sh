#!/bin/sh

# tcprewrite --dlt=enet -i magic.pcap -o magic-1.pcap
tcpreplay -i wlan0 -l 0 magic.pcap 
