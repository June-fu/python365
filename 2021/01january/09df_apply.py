#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-11 23:03:08
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-11 23:03:10
 # @ Description:
 '''

import datetime
import pandas as pd
import numpy as np

df = pd.DataFrame([
    ['2021-07-09', datetime.datetime(2021, 3, 2)]] * 2, dtype='O')

print(df)
print(df.apply(pd.to_datetime))

df1 = pd.DataFrame([['1.1', 2, 3]] * 2, dtype='O')
print(df1)
print(df1.apply(pd.to_numeric))

df2 = pd.DataFrame([['5us', pd.Timedelta('1day')]] * 2, dtype='O')
print(df2)
print(df2.apply(pd.to_timedelta))