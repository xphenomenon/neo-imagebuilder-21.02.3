#!/usr/bin/env bash

make image FILES="files" PROFILE=friendlyarm_nanopi-neo \
    DISABLED_SERVICES="dnsmasq odhcpd uhttpd" \
    PACKAGES="kmod-cfg80211 kmod-mac80211 iperf iperf3 \
    sshfs scapy tcpreplay hostapd-openssl wpa-supplicant-p2p tcpdump rpcapd kmod-usb-core usbutils wireless-tools zram-swap \
    wpa-cli hostapd-utils dmesg coreutils-tee usb-modeswitch \
    kmod-rtw88-usb kmod-rtl8812au-ac aircrack-ng kmod-rtl8188eu mdk4 \
    kmod-rtl8192fu arp-scan arp-scan-database nmap kmod-mt7601u kmod-rtl8821cu \
    openssh-sftp-server tmux vim git rsync make isc-dhcp-client-ipv4 kmod-rtl8192cu \
    kmod-mt76x2u kmod-rtl8852bu perl iwinfo fdisk dtc less minicom"
