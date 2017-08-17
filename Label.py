#!/usr/bin/python
## 2.Label Script
###############################################

import csv
from math import sin, cos, sqrt, atan2, radians

reader1=csv.reader(open('CleanedData_noheader.csv', 'r'), delimiter=',')
reader2=csv.reader(open('POIlist_noheader.csv', 'r'), delimiter=',')
writer=csv.writer(open('Labeloutput.csv', 'w'), delimiter=',')
entries = set()
seclist = list(reader2)

# approximate radius of earth in km
R = 6373.0
count=0

## Reading cleaned Datasample file
for row in reader1:
    lg=float(row[5])
    lt=float(row[6])
    lat1 = radians(lg)
    lon1 = radians(lt)    
    count = 1
    smallestdistance = 0.0  
## Reading POI list file 
## Calculating the distance between incoming record and 
## POI location and finding out the minimum distance
    for irow in seclist:      
        i_poi=irow[0]
        i_lg=float(irow[1])
        i_lt=float(irow[2])
        lat2 = radians(i_lg)
        lon2 = radians(i_lt)  
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c        
        if ( (count == 1) or (distance < smallestdistance ) ):         
           smallestdistance = distance
           poi_s = i_poi           
           count = count + 1
                
   ## Output file with assigned POI location and its minumum distance
    writer.writerow(row+[smallestdistance,poi_s])