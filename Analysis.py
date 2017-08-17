#!/usr/bin/python
## 3.1 & 3.2 Analysis
###############################################

import csv
import statistics
from math import pi
poi1list=[]
poi2list=[]
poi3list=[]
poi4list=[]
## Function to calcualte mean, stddeviation,radius and density for each POI location
def calc(poilist):
    POImean=statistics.mean(poilist)
    POIstddev=statistics.stdev(poilist)
    radiusPOI=max(poilist)
    areapoi = (pi * (radiusPOI ** 2))
    density =  len(poilist)/areapoi
    return (POImean,POIstddev,radiusPOI,areapoi,density)

def printvalues(mean,stddev,radius,density):
    print ("POI MEAN:%s,POI STDDEV %s,POI RADIUS:%s, DENSITY:%s" %(mean,stddev,radius,density)) 

# Forming  smallest distances list for each POI location 
# from the file generated in second solution
reader1=csv.reader(open('Labeloutput.csv', 'r'), delimiter=',')
for row in reader1:
    POI=row[-1]
    DI=float(row[-2])
    if (POI == 'POI1'):
        poi1list.append(DI)
    elif (POI == 'POI2'):
        poi2list.append(DI)
    elif  (POI == 'POI3'):
        poi3list.append(DI)
    elif  (POI == 'POI4'):
       poi4list.append(DI)

Calulated_poi1_values=calc (poi1list)
print  ("POI1 values are")
printvalues (Calulated_poi1_values[0],Calulated_poi1_values[1],Calulated_poi1_values[2],Calulated_poi1_values[4])

Calulated_poi2_values=calc (poi2list)
print  ("POI2 values are")
printvalues (Calulated_poi2_values[0],Calulated_poi2_values[1],Calulated_poi2_values[2],Calulated_poi2_values[4])

Calulated_poi3_values=calc (poi3list)
print  ("POI3 values are")
printvalues (Calulated_poi3_values[0],Calulated_poi3_values[1],Calulated_poi3_values[2],Calulated_poi3_values[4])

Calulated_poi4_values=calc (poi4list)
print  ("POI4 values are")
printvalues (Calulated_poi4_values[0],Calulated_poi4_values[1],Calulated_poi4_values[2],Calulated_poi4_values[4])
