#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-21 23:39:51
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-21 23:39:54
 # @ Description:
If a subset of data is being parsed using the usecols option, 
the index_col specification is based on that subset, not the original data.
 '''
import pandas as pd
from io import StringIO

data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')
df = pd.read_csv(StringIO(data))
print(df)

print(pd.read_csv(StringIO(data), usecols=['b', 'c']))

print(pd.read_csv(StringIO(data), usecols=['b', 'c'], index_col=0))