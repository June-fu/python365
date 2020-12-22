#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-27 23:19:25
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-27 23:19:30
 # @ Description:
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})
print(df)

# Note that by chance some NumPy methods, like mean, std, and sum,will exclude NAs on Series input by default
print(np.mean(df['one']))
print(np.mean(df['one'].to_numpy()))

# Series.nunique() will return the number of unique non-NA values in a Series
s = pd.Series(np.random.randn(500))
s[20:500] = np.nan
s[10:20] = 5
print(s.nunique())