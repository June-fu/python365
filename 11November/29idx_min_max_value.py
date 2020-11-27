#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-28 00:35:15
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-28 00:35:25
 # @ Description: index of min/max values
 The idxmin() and idxmax() functions on Series and DataFrame compute the index
 labels with the minimum and maximum corresponding values
 '''
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5))
print(s)

print(s.idxmin(), s.idxmax())

df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
print(df)

print(df.idxmin(axis=0))
print(df.idxmax(axis=1))

# when there are multiple rows(or columns) matching the minimum or maximum value
# idxmin() and idxmax() return the first matching index
df2 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=['A'], index=list('edcba'))
print(df2)
print(df2['A'].idxmin())