# -*- coding: utf-8 -*-
"""
Spyder Editor

Authors: Jason Teng, Seung Son
"""

from urllib import request
import json
import argparse
from math import sin, asin, cos, sqrt, atan2, radians

parser = argparse.ArgumentParser(description='Replica locator for project 5.')
parser.add_argument('ip', help='the ip to reference against')
args = parser.parse_args()

ip = args.ip

replicas = [
        '54.186.185.27',
        '54.199.204.174',
        '54.72.143.213',
        '54.84.248.26']

replica_locs = []

for r in replicas:
    res = json.loads(request.urlopen('http://ip-api.com/json/' + r).read().decode())
    replica_locs.append((res['lat'], res['lon']))

res = json.loads(request.urlopen('http://ip-api.com/json/' + ip).read().decode())
iploc = (res['lat'], res['lon'])

def distance(c1, c2):
    lat1 = c1[0]
    lon1 = c1[1]
    lat2 = c2[0]
    lon2 = c2[1]
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

closest = replicas[0]
d = distance(iploc, replica_locs[0])
for i in range(len(replicas)):
    new_d = distance(iploc, replica_locs[i])
    if new_d  < d:
        closest = replicas[i]
        d = new_d

print(closest)
