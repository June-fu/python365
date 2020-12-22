#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-26 20:33:26
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-26 20:35:41
 # @ Description:descriptive statistics
 Most of these are aggregations (hence producing a lower-dimensional result) like sum(), mean(), and quantile(), but some of them, like cumsum() and cumprod(), produce an object of the same size
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

print(df)
# DataFrame: “index” (axis=0, default), “columns” (axis=1)
print(df.mean(0))
print(df.mean())

print(df.mean(1))

# All such methods have a skipna option signaling whether to exclude missing data (True by default)
print(df.sum(0, skipna=False))
print(df.sum(axis=1, skipna=True))

# Combined with the broadcasting / arithmetic behavior
ts_stand = (df - df.mean()) / df.std()

print(ts_stand.std())

xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
print(xs_stand.std(1))

# Note the methods like cumsum() and cumprod() preserve the location of NaN values
print(df.cumsum())
print(df.cummax())