#!/usr/bin/python3
import time
import json
from datetime import datetime, date, timedelta


#Enter your longitude here and copy the Length of a Degree of Latittude/Longitude in Metres
lod_lat = 111061.57849146728
lod_long = 83627.11630547515
lat_per_metre = 1/lod_lat
long_per_metre = 1/lod_long

with open('/home/adam/Desktop/1587822189712.json', encoding='utf-8-sig') as json_file:
  data = json.loads(json_file.read().replace('\n', ''))

tgt_location = {}
tgt_location['latitude'] = 41.3979457
tgt_location['longitude'] = 2.15831900
tgt_time = datetime.fromtimestamp(1587808852000/1000)
start_time = tgt_time - timedelta(hours=4)
end_time = tgt_time + timedelta(hours=4)
print("Start of window: " + str(start_time))
print("End of window: " + str(end_time))

hits = 0

for pt in data:
    long_diff = abs(tgt_location['longitude'] - pt['longitude'])
    lat_diff = abs(tgt_location['latitude'] - pt['latitude'])
    if long_diff < (20 * long_per_metre):
        if lat_diff < (20 * lat_per_metre):
            dt = datetime.fromtimestamp(pt['time'] / 1000.0)
            if dt > start_time and dt < end_time:
                print("Point of concern identified... " + str(long_diff / long_per_metre) + "m & " + str(lat_diff / lat_per_metre) +"m & " + str(dt - tgt_time))
