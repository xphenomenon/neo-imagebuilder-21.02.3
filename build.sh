#!/usr/bin/env bash

make image FILES="files" PROFILE=friendlyarm_nanopi-neo \
    DISABLED_SERVICES="dnsmasq odhcpd uhttpd" \
    PACKAGES="kmod-cfg80211 kmod-mac80211 iperf iperf3 autossh openvpn-openssl \
    sshfs scapy tcpreplay wpad-openssl tcpdump rpcapd kmod-usb-core usbutils gdb gdbserver wireless-tools zram-swap \
    wpa-cli hostapd-utils dmesg coreutils-tee luci usb-modeswitch"
