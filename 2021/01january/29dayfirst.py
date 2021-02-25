#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-25 22:31:47
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-25 22:31:53
 # @ Description:
 infer_datetime_format is sensitive to dayfirst
 '''

import pandas as pd
from io import StringIO

# dayfirst argument
data = ('date,A,B,C\n'
'01/12/2009,a,1,2\n'
'20090102,b,3,4\n'
'20090103,c,4,5')

df = pd.read_csv(StringIO(data), index_col=0, parse_dates=True, infer_datetime_format=True)
print(df)

# set dayfirst 
df2 = pd.read_csv(StringIO(data), index_col=0, parse_dates=True, infer_datetime_format=True, dayfirst=True)
print(df2)