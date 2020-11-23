#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-23 23:08:05
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-23 23:08:08
 # @ Description:Comparing if objects are equivalent
 '''
import pandas as pd
import numpy  as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})
print(df)

print(df + df)
print(df * 2)
# NaNs do not compare as equals
print(df + df == df * 2)

print((df + df == df * 2).all())

# NDFrames (such as Series and DataFrames) have an equals() method for testing equality, 
# with NaNs in corresponding locations treated as equal
print((df + df).equals(df * 2))

# Note that the Series or DataFrame index needs to be in the same order for equality to be True:
df1 = pd.DataFrame({'col': ['foo', 0, np.nan]})
df2 = pd.DataFrame({'col': [np.nan, 0, 'foo']}, index=[2, 1, 0])
# False because the index is not in the same order
print(df1.equals(df2))
print(df1.equals(df2.sort_index()))