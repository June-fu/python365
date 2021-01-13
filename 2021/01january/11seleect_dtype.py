#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-13 21:47:27
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-13 21:47:29
 # @ Description: Selecting columns based on dtype
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'string': list('abc'),
    'int64': list(range(1, 4)),
    'uint8': np.arange(3, 6).astype('u1'),
    'float64': np.arange(4.0, 7.0),
    'bool1': [True, False, True],
    'bool2': [False, True, False],
    'dates': pd.date_range('now', periods=3),
    'categroyp': pd.Series(list("ABC")).astype('category')
})

df['tdeltas'] = df.dates.diff()
df['uint64'] = np.arange(3, 6).astype('u8')
df['other_dates'] = pd.date_range('20210101', periods=3)
df['tz_aware_dates'] = pd.date_range('20210101', periods=3, tz='US/Eastern')
print(df)

print(df.dtypes)

# select_dtypes() has two parameters: include() and exclude
print(df.select_dtypes(include=[bool]))
# You can also pass the name of a dtype in the NumPy dtype hierarchy:
print(df.select_dtypes(include=['bool']))
print(df.select_dtypes(include=['number', 'bool'], exclude=['unsignedinteger']))

# to select string columns you must use the object dtype
print(df.select_dtypes(include=['object']))