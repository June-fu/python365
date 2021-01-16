#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-16 23:34:32
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-16 23:34:34
 # @ Description:
 '''

import pandas as pd
import numpy as np
from io import StringIO

data = ('a,b,c,d\n'
         '1,2,3,4\n'
         '5,6,7,8\n'
         '9,10,11')
print(data)

df = pd.read_csv(StringIO(data), dtype='object')
print(df)

# you can indicate the data type for the whole DataFrame or individual columns
df = pd.read_csv(StringIO(data), dtype={'b': object, 'c': np.float64, 'd': 'Int64'})
print(df.dtypes)

# you can use the converters argument of read_csv():
data2 = ("col_1\n"
        "1\n"
        "2\n"
        "'A'\n"
        "4.22")
df = pd.read_csv(StringIO(data2), converters={'col_1': str})
print(df)
print(df['col_1'].apply(type).value_counts())

df2 = pd.read_csv(StringIO(data2))
df2['col_1'] = pd.to_numeric(df2['col_1'], errors='coerce')
print(df2)
print(df2['col_1'].apply(type).value_counts())