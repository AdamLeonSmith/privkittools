import json
from datetime import datetime, date
import time
epoch = datetime.utcfromtimestamp(0)

#This script takes years of google location data in, converts it to privkit format, and uses the data to create MANY files all representing March 2020

def unix_time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)

#Change the input file name in the following line
with open('in.json', encoding='utf-8-sig') as json_file:
    json_data = json.loads(json_file.read().replace('\n', ''))
    ret = []
    total = len(json_data['locations'])
    print('Found ' + str(total) + ' locations')
    count = 0
    last_time = 0
    file = 0
    diffs = []
    last_month = 0
    day_of_month = 1

    for punto in json_data['locations']:
        out = {}
        print(count, "/", total, " locations checked")
        count = count + 1
        out['time'] = int(punto['timestampMs'])
        ms = int(punto['timestampMs'])


        if count > 1:
            diff = int(out['time']) - int(last_time)
            print("diff: " + str(diff))
            diffs.append(diff)

        #modify the timestamp
        month = str(datetime.fromtimestamp(float(ms) / 1000.0).month)
        act_day = str(datetime.fromtimestamp(float(ms) / 1000.0).day)
        if len(month) == 1:
            month = "0" + month
        _date = datetime(2020,3,int(day_of_month),
                    datetime.fromtimestamp(float(ms) / 1000.0).hour,
                    datetime.fromtimestamp(float(ms) / 1000.0).minute,
                    datetime.fromtimestamp(float(ms) / 1000.0).second,
                    datetime.fromtimestamp(float(ms) / 1000.0).microsecond)
        out['time'] = unix_time_millis(_date)


        #modify the format of the location
        out['latitude'] = float(punto['latitudeE7']) / 10000000
        out['longitude'] = float(punto['longitudeE7']) / 10000000

        ret.append(out)

        #if we roll into a new month reset the date
        if month != last_month:
            f = open('privkit'+str(file)+'.json', 'w')
            f.write(json.dumps(ret))
            f.close()
            file = file + 1
            ret = []
            day_of_month = 1
        elif act_day != last_day:
            day_of_month = day_of_month + 1

        last_month = month
        last_day = act_day

    total = 0
    for diff in diffs:
        total = total + diff
    print("Average difference in data point timings: " + str(total/count))
