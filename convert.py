import json
from datetime import datetime, date
import time

with open('/home/adam/Desktop/Jan_ghist_2020_APRIL.json', encoding='utf-8-sig') as json_file:
    json_data = json.loads(json_file.read().replace('\n', ''))
    ret = []
    total = len(json_data['locations'])
    print('Found ' + str(total) + ' locations')
    count = 0
    last_time = 0
    diffs = []
    for punto in json_data['locations']:
        out = {}
        print(count, "/", total, " locations checked")
        count = count + 1
        out['time'] = int(punto['timestampMs'])

        if count > 1:
            diff = int(out['time']) - int(last_time)
            print("diff: " + str(diff))
            diffs.append(diff)

        last_time = out['time']
        month = str(datetime.fromtimestamp(float(out['time']) / 1000.0).month)
        out['latitude'] = float(punto['latitudeE7']) / 10000000
        out['longitude'] = float(punto['longitudeE7']) / 10000000
        ret.append(out)
    f = open('jan_long.json', 'w')
    f.write(json.dumps(ret))
    f.close()

    total = 0
    for diff in diffs:
        total = total + diff
    print("Average difference in data point timings: " + str(total/count))
