#!/usr/bin/python3
import time
import json
from datetime import datetime, date, timedelta
import math

#Enter your latitude here: http://www.csgnetwork.com/degreelenllavcalc.html
# then copy the Length of a Degree of Latittude/Longitude in Metres
lod_lat = 111061.57849146728
lod_long = 83627.11630547515
lat_per_metre = 1/lod_lat
long_per_metre = 1/lod_long

with open('/home/adam/Desktop/1587822189712.json', encoding='utf-8-sig') as json_file:
  data = json.loads(json_file.read().replace('\n', ''))

tgt_location = {}
tgt_location['latitude'] = 41.39808000
tgt_location['longitude'] = 2.1582888
tgt_time = datetime.fromtimestamp(1587808852000/1000)
start_time = tgt_time - timedelta(hours=4)
end_time = tgt_time + timedelta(hours=4)
print("Start of window: " + str(start_time))
print("End of window: " + str(end_time))

hits = 0

for pt in data:
    long_diff = abs(tgt_location['longitude'] - pt['longitude'])
    lat_diff = abs(tgt_location['latitude'] - pt['latitude'])
    _long_diff = long_diff * lod_long
    _lat_diff = lat_diff * lod_lat
    dist = math.sqrt(_long_diff * _long_diff + _lat_diff * _lat_diff)
    if dist < 20:
        dt = datetime.fromtimestamp(pt['time'] / 1000.0)
        if dt > start_time and dt < end_time:
            print("Point of concern identified... " + str(dist) +"m & " + str(dt - tgt_time))
