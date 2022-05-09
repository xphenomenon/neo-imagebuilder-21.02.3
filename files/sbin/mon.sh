#!/bin/sh

ifconfig wlan0 up
iw dev wlan0 set monitor none
iw dev wlan0 set channel 1 HT20
