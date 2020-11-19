#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-19 20:22:07
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-19 20:22:42
 # @ Description:For broadcasting behavior, Series input is of primary interest. 
 # Using these functions, you can use to either match on the index or columns via the axis keyword
 '''
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

print(df)

row = df.iloc[1]
print(row)

column = df['two']
print(column)

# default sub()
print(df.sub(row))

print(df.sub(row, axis=1))
print(df.sub(row, axis='columns'))

# the axis default is 1
print(df.sub(column, axis='index'))
print(df.sub(column, axis=0))

