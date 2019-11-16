#!/usr/bin/bash

if [[ $(grep -c -e "^nameserver 192.168.1.1$" /etc/resolv.conf) -eq 1 && $(grep -c -e "^nameserver 192.168.1.2$" /etc/resolv.conf) -eq 1 && $(grep -c -e "^nameserver 10.20.10.30$" /etc/resolv.conf) -eq 1 && $(grep -c -e "^nameserver 10.20.10.31$" /etc/resolv.conf) -eq 1 && $(grep -c -e "^search opensource.com$" /etc/resolv.conf) -eq 1 ]]; then
    exit 0
else
    exit 1
fi
