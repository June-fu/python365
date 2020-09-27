#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/27
"""
DataFrame interoperability with NumPy functions
Elementwise NumPy ufuncs (log, exp, sqrt, …) and various other NumPy functions
can be used with no issues on Series and DataFrame, assuming the data within are numeric:
"""
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2020', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index)
print(np.exp(df))
print(np.asarray(df))

ser = pd.Series([1, 2, 3, 4])
print(ser)
print(np.exp(ser))


# When multiple Series are passed to a ufunc, they are aligned before performing the operation.
ser1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser2 = pd.Series([1, 3, 5], index=['b', 'a', 'c'])

print(ser2 + ser1)
print(np.remainder(ser1, ser2))

# As usual, the union of the two indices is taken, and non-overlapping values are filled with missing values.
ser3 = pd.Series([2, 4, 6], index=list('bcd'))
print(np.remainder(ser1, ser3))

# When a binary ufunc is applied to a Series and Index,
# the Series implementation takes precedence and a Series is returned.
ser = pd.Series([1, 2, 3])
idx = pd.Index([4, 5, 6])
print(np.maximum(ser, idx))