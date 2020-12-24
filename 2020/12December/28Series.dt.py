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

s = pd.Series(pd.date_range('20200101 09:10:12', periods=4))
print(s)

print(s.dt.hour)
print(s.dt.second)
print(s.dt.day)

# This enables nice expressions like this
print(s[s.dt.day == 2])
# you can easily produces tz aware transformations
stz = s.dt.tz_localize('US/Eastern')
print(stz.dt.tz)

# You can also chain these types of operations:
print(s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern'))
