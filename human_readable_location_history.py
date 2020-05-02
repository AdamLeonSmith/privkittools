#!/usr/bin/python3
import time
import json
from datetime import datetime, date, timedelta


with open('/home/adam/Desktop/adam1587916406685.json', encoding='utf-8-sig') as json_file:
  data = json.loads(json_file.read().replace('\n', ''))


for pt in data:
  print("Timestamp:" + str(pt['time']) + " Time: " + str(datetime.fromtimestamp(pt['time'] / 1000.0)) + " lat: " + str(pt['latitude']) + " long: " + str(pt['longitude']))
