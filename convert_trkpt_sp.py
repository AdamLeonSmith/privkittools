#!/usr/bin/python3
from datetime import datetime
import dateutil.parser
import json
import xml.etree.ElementTree as ET
root = ET.parse('/home/adam/Desktop/mrg.gpx').getroot()
output = []
for type_tag in root.findall('trkpt'):
    ret = {}
    ret['latitude']= float(type_tag.get('lat'))
    ret['longitude']= float(type_tag.get('lon'))
    ret['time']= int(dateutil.parser.parse(type_tag.findtext('time')).timestamp()*1000)
    output.append(ret)
print(json.dumps(output))
