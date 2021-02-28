#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-28 22:18:07
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-28 22:18:09
 # @ Description:
 The parameter float_precision can be specified in order to use a specific floating-point converter during parsing with the C engine. 
 '''

import pandas as pd
from io import StringIO

val = '0.3066101993807095471566981359501369297504425048828125'
print(float(val))
data = 'a,b,c\n1,2,{0}'.format(val)
df = pd.read_csv(StringIO(data), engine='c', float_precision=None)
print(df['c'][0])
print(abs(df['c'][0] - float(val)))

df2 = pd.read_csv(StringIO(data), engine='c', float_precision='high')
print(df2['c'][0])
print(abs(df2['c'][0] - float(val)))

df3 = pd.read_csv(StringIO(data), engine='c', float_precision='round_trip')
print(df3['c'][0])
print(abs(df3['c'][0] - float(val)))