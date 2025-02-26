#!/usr/bin/env python
import os
from soco import SoCo
import time
from netdisco.discovery import NetworkDiscovery
import urllib3

netdis = NetworkDiscovery()

netdis.scan()

for dev in netdis.discover():
    if dev == 'sonos':
        for player in netdis.get_info(dev):
            print(SoCo(player).ip_address)

netdis.stop()