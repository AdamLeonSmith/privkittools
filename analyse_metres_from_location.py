#!/usr/bin/python3
import time
import json
from datetime import datetime, date, timedelta


with open('/home/adam/Desktop/1587822189712.json', encoding='utf-8-sig') as json_file:
  data = json.loads(json_file.read().replace('\n', ''))

tgt_location = {}
tgt_location['latitude'] = 41.39792327
tgt_location['longitude'] = 2.15831900
tgt_time = datetime.fromtimestamp(1587794453000/1000)
start_time = tgt_time - timedelta(hours=4)
end_time = tgt_time + timedelta(hours=4)
print("Start of window: " + str(start_time))
print("End of window: " + str(end_time))

hits = 0

for pt in data:
    long_diff = abs(tgt_location['longitude'] - pt['longitude'])
    lat_diff = abs(tgt_location['latitude'] - pt['latitude'])
    if long_diff < 0.0002:
        if lat_diff < 0.0002:
            dt = datetime.fromtimestamp(pt['time'] / 1000.0)
            if dt > start_time and dt < end_time:
                print("Point of concern identified... " + str(long_diff / 0.00001) + "m & " + str(lat_diff / 0.00001) +"m & " + str(dt - tgt_time))
