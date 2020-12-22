#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-22 13:21:45
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-22 13:21:49
 # @ Description:Boolean reductions
 You can apply the reductions: empty, any(), all(), and bool() to provide a way to summarize a boolean result
 '''
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})
print(df)

print("all:\n", (df > 0).all())
print("empty:\n", (df > 0).empty)
print("any:\n", (df > 0).any())

# you can reduce to a final boolean value
print((df >0).any().any())

# you can test if a pandas object is empty, via the empty property
print("test df is empty or not:\n", df.empty)
print(pd.DataFrame(columns=list('ABC')).empty)

# to evaluate single-element pandas objects in a boolean context, use the method bool()
print("evaluate single-element of Series:\n", pd.Series([True]).bool())
print(pd.Series([False]).bool())

print("evaluate single-element of DataFrame:\n", pd.DataFrame([[True]]).bool())
print(pd.DataFrame([[False]]).bool())