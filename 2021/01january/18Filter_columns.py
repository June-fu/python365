#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-29 23:18:46
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-29 23:18:49
 # @ Description:
 Filtering columns(usecols)
 '''

import pandas as pd
from io import StringIO

data = 'a,b,c,d\n1,2,3,foo\n4,5,6,bar\n7,8,9,baz'
print(pd.read_csv(StringIO(data)))

print(pd.read_csv(StringIO(data), usecols=['b', 'd']))
print(pd.read_csv(StringIO(data), usecols=[0, 2, 3]))
print(pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['A', 'B', 'C']))

# the usecols argument can also be used to specify which columns to use in the final result
print(pd.read_csv(StringIO(data), usecols=lambda x: x not in ['a', 'c']))