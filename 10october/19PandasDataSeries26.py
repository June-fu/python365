#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-07 22:23:30
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-07 22:23:33
 # @ Description:
 Write a Pandas program to convert a series of date strings to a timeseries
 '''
import pandas as pd

s = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:,\n", s)

print("Series of date strings to a timeseries:\n", pd.to_datetime(s))