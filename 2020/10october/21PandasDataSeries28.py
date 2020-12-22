#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-09 21:44:20
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-09 21:44:22
 # @ Description:
 Write a Pandas program to get the day of month, day of year, week number 
 and day of week from a given series of date strings
 '''
import pandas as pd
from dateutil.parser import parse

s = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:\n", s)

date_series = s.map(lambda x: parse(x))
print(date_series)

print("Day of month:\n", date_series.dt.day.tolist())
print("Day of year:\n", date_series.dt.dayofyear.tolist())
print("week number:\n", date_series.dt.weekofyear.tolist())
print("Day of week:\n", date_series.dt.weekday.tolist())