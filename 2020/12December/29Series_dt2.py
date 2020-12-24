#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-24 22:22:32
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-24 22:22:35
 # @ Description:
Series has an accessor to succinctly return datetime like properties for the values of the Series
 '''

import pandas as pd

# format datetime values strings with Series.dt.strftime() which supports same format as the standard strftime()
s = pd.Series(pd.date_range('20200101', periods=4))
print(s)

print(s.dt.strftime('%Y/%m/%d'))

# the .dt accessor works for period and timedelta dtypes
s1 = pd.Series(pd.date_range('20200101', periods=4, freq='D'))
print(s1)
print(s1.dt.year, s1.dt.day, sep='\n')
# timedelta
s2 = pd.Series(pd.timedelta_range('1 day 00:00:05', periods=4, freq='s'))
print(s2)
print(s2.dt.days, s2.dt.seconds, s2.dt.components, sep='\n')
