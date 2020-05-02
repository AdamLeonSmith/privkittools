#!/usr/bin/python3
import csv
import json
import os

dir = '/home/adam/Desktop/synth'
os.chdir(dir)
for filename in os.listdir(dir):
    if filename.endswith(".csv"):
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            n = 0
            output = []
            for row in csvReader:
                if n > 0:
                    ret = {}
                    ret['latitude']= float(row[1])
                    ret['longitude']= float(row[2])
                    ret['time']= int(float(row[0]))
                    output.append(ret)
                n = n+1
        with open(filename.replace('csv', 'json'), 'w') as outfile:
            json.dump(output, outfile)
