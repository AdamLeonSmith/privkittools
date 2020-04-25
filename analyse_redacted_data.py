#!/usr/bin/python3
import time
import json
import numpy as np

with open('/home/adam/Downloads/dean1-REDACTED.json', encoding='utf-8-sig') as json_file:
  data = json.loads(json_file.read().replace('\n', ''))

long = []
lat = []
times = []
count = 0
last_time = 0
diffs = []

for pt in data:
  count = count + 1
  lat.append(pt['latitude'])
  long.append(pt['longitude'])
  t = pt['time']
  if count > 1:
        diff = t - last_time
        print("diff: " + str(diff))
        diffs.append(diff)
  last_time = t

total=0
for diff in diffs:
     total = total + diff

print("Mean average difference in data point timings: " + str(total/count/1000/60) + " mins")
print("Standard deviation of data point timings: " + str(np.std(diffs)/1000/60) + " mins")
print("Standard deviation of longitude: " + str(np.std(long)/0.00001) + "m")
print("Standard deviation of latitude: " + str(np.std(lat)/0.00001) + "m")
