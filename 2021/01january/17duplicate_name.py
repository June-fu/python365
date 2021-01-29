#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-29 23:15:52
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-29 23:15:53
 # @ Description:
mangle_dupe_cols=True
 '''

import pandas as pd
from io import StringIO

data = ('a,b,a\n'
         '0,1,2\n'
         '3,4,5')
print(pd.read_csv(StringIO(data)))

print(pd.read_csv(StringIO(data), mangle_dupe_cols=False))