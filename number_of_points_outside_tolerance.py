#!/usr/bin/python3
import time
import json
from datetime import datetime, date, timedelta
import math

#Enter your latitude here: http://www.csgnetwork.com/degreelenllavcalc.html
# then copy the Length of a Degree of Latittude/Longitude in Metres
lod_lat = 111061.59
lod_long = 83626.24
lat_per_metre = 1/lod_lat
long_per_metre = 1/lod_long
tolerance = 20 #metres

with open('/home/adam/Downloads/gpx-REDACTED.json', encoding='utf-8-sig') as json_file:
  data = json.loads(json_file.read().replace('\n', ''))

#calculate average position
n = 0
tot_lon = 0
tot_lat = 0
for pt in data:
    tot_lon = tot_lon + pt['longitude']
    tot_lat = tot_lat + pt['latitude']
    n = n + 1
tgt_location = {}
tgt_location['latitude'] = tot_lat / n
tgt_location['longitude'] = tot_lon / n

hits = 0

for pt in data:
    long_diff = abs(tgt_location['longitude'] - pt['longitude'])
    lat_diff = abs(tgt_location['latitude'] - pt['latitude'])

    _long_diff = long_diff * lod_long
    _lat_diff = lat_diff * lod_lat

    dist = math.sqrt(_long_diff * _long_diff + _lat_diff * _lat_diff)
    if dist > 20:
        print("Outlier identified... " + str(dist) +"m")
