#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-22 23:59:17
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-22 23:59:19
 # @ Description:arguments parse_dates
 '''

import pandas as pd
from io import StringIO

data =('date,A,B,C\n'
'20090101,a,1,2\n'
'20090102,b,3,4\n'
'20090103,c,4,5')

# arguments parse_dates
df = pd.read_csv(StringIO(data), index_col=0, parse_dates=True)
print(df)

# These are Python datetime objects
print(df.index)