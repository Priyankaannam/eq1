#!/usr/bin/python
##1. CLeanup Script
###############################################

import csv

writer=csv.writer(open('CleanedData.csv', 'w'), delimiter=',')
reader=csv.reader(open('DataSample.csv', 'r'), delimiter=',')
entries = set()
dups  = set()

## Identfying records which have identical `geoinfo` and `timest`
for row in reader:
    key = (row[1], row[5], row[6])
    if key not in entries:
       entries.add(key)      
    else:
       dups.add(key)

## Eleminating the suspicous data from the data set
reader=csv.reader(open('DataSample.csv', 'r'), delimiter=',')  
for out in reader: 
    keys = (out[1], out[5], out[6])
    if keys not in dups:
       writer.writerow(out)   
