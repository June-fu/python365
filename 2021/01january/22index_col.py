#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-21 23:39:51
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-21 23:39:54
 # @ Description:
If a file has one more column of data than the number of column names,
 the first column will be used as the DataFrame’s row names:
 '''

import pandas as pd
from io import StringIO

data = ('a,b,c\n'
         '4,apple,bat,5.7\n'
         '8,orange,cow,10')

df = pd.read_csv(StringIO(data))
print(df)

# you can achieve this behavior using the index_col option.
data2 = ('index,a,b,c\n'
         '4,apple,bat,5.7\n'
         '8,orange,cow,10')
df2 = pd.read_csv(StringIO(data2), index_col=0)
print(df2)

# you can achieve this behavior using the index_col option.you should explicitly disable the index column
data3 = ('a,b,c\n'
         '4,apple,bat,\n'
         '8,orange,cow,')
df3 = pd.read_csv(StringIO(data3), index_col=False)

print(df3)