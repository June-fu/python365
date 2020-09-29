#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/22
"""
Attributes and underlying data
"""
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2020', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index)

print(df[:2])
# shape: gives the axis dimensions of the object, consistent with ndarray
print(df.shape)

# Series: index (only axis)
ser = pd.Series([1, 2, 3, 4])
print(ser)
print(ser.index)

# DataFrame: index (rows) and columns
print(df.index)
print(df.columns)

df.columns = [x > 0 for x in df.columns]
print(df)

# To get the actual data inside a Index or Series, use the .array property
print(ser.array)
print(df.index.array)

# If you know you need a NumPy array, use to_numpy() or numpy.asarray().
print('########')
print(ser.to_numpy())
print(np.asarray(ser))
