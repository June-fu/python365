#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/8/31
"""
Series is ndarray-like
"""
import numpy as np
import pandas as pd

# Series is ndarray-like
# Series acts very similarly to ndarray , and is a valid argument to most NumPy functions.
s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s[0])
print("s[:3]:\n", s[:3])
print("s[s > s.median]\n", s[s > s.median()])
print("s[[4, 3, 1]]\n", s[[4, 3, 1]])
print(np.exp(s))

# Like a NumPy array, a pandas Series has a dtype.
print(s.dtype)

# If you need the actual array backing a Series, use Series.array.
print(s.array)

# While Series is ndarray-like, if you need an actual ndarray, then use Series.to_numpy().
print(s.to_numpy())
