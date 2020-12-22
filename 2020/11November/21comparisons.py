#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-22 13:21:45
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-22 13:21:49
 # @ Description:Series and DataFrame have the binary comparison methods eq, ne, lt, gt, le, and ge 
 Flexible comparisons
 '''
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})
print(df)

df2 = df.copy()
df2['three']['a'] = 1.0
print(df2)

print(df.gt(df2))
print(df2.ne(df))
