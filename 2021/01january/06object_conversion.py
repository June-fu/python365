#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-05 21:52:09
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-05 21:52:12
 # @ Description:
 '''

import pandas as pd
import datetime 

# infer_objects() can be used to soft convert to the correct type

df = pd.DataFrame([
    [1, 2],
    ['a', 'b'],
    [datetime.datetime(2016, 3, 2),
    datetime.datetime(2016, 3, 2)]
])

print(df)
df = df.T
print(df)
print(df.dtypes)

# Because the data was transposed the original inference stored all columns as object,
#  which infer_objects will correct.
print(df.infer_objects().dtypes)

# to_numberic() conversion to numberic dtypes
m = ['1.1', 2, 3]
print(pd.to_numeric(m))

# to_datetime() conversion to datetime objects
n = ['2021-01-01', datetime.datetime(2021, 1, 5)]
print(pd.to_datetime(n))

# to_timedelta() conversion to timedelta objects
x = ['5us', pd.Timedelta('1day')]
print(pd.to_timedelta(x))