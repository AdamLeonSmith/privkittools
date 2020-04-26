#!/usr/bin/python3
import math

lat_a = 53.35550673486802
long_a = -1.486858875056597
lat_b = 53.3570432
long_b = -1.4913927

#Enter your latitude here: http://www.csgnetwork.com/degreelenllavcalc.html
# then copy the Length of a Degree of Latittude/Longitude in Metres
lod_lat = 111292.91
lod_long = 66584.44
long_diff = abs(long_a - long_b) * lod_long
lat_diff = abs(lat_a - lat_b) * lod_lat
print(str(math.sqrt(long_diff * long_diff + lat_diff * lat_diff)) + "metres")
