#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-19 20:51:24
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-19 20:51:29
 # @ Description:
 '''
import pandas as pd
import numpy as np

#Furthermore you can align a level of a MultiIndexed DataFrame with a Series.
df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

column = df['two']
print(column)

dfmi = df.copy()
dfmi.index = pd.MultiIndex.from_tuples([(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a')], names=['first', 'second'])
print(dfmi)

print(dfmi.sub(column, axis=0, level='second'))
