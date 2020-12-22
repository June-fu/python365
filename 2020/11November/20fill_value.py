#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-20 23:05:34
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-20 23:05:37
 # @ Description:In Series and DataFrame, the arithmetic functions have the option of inputting a fill_value
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

print(df + df2)

print(df.add(df2, fill_value=0))

#you can later replace NaN with some other value using fillna if you wish
print(df.fillna(2))