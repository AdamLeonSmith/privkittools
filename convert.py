import json
from datetime import datetime, date
import time


with open('test.json', encoding='utf-8-sig') as json_file:
    json_data = json.loads(json_file.read().replace('\n', ''))
    ret = []
    total = len(json_data['locations'])
    print('Found ' + str(total) + ' locations')
    count = 0
    for punto in json_data['locations']:
        out = {}
        print(count, "/", total, " locations checked")
        count = count + 1
        out['time'] = punto['timestampMs']
        month = str(datetime.fromtimestamp(float(out['time']) / 1000.0).month)
        if len(month) == 1:
            month = "0" + month
        out['latitude'] = float(punto['latitudeE7']) / 10000000
        out['longitude'] = float(punto['longitudeE7']) / 10000000
        ret.append(out)
    f = open('privkit.json', 'w')
    f.write(str(ret))
    f.close()
