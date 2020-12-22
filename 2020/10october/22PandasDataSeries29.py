#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-09 21:58:39
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-09 21:58:41
 # @ Description:
 Write a Pandas program to convert year-month string to dates
  adding a specified day of the month
 '''

import pandas as pd
from dateutil.parser import parse

s = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("Original Series:\n", s)

date_series = s.map(lambda x: parse('11' + x))
print("New dates:\n", date_series)