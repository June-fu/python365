#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-01 22:55:26
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-01 22:55:28
 # @ Description:
 Arbitrary functions can be applied along the axes of a DataFrame using the apply() method
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})
print(df)

print(df.apply(np.mean))
print(df.apply(np.mean, axis=1))

print("Max-Min:\n", df.apply(lambda x: x.max()-x.min()))
print("cumsum:\n", df.apply(np.cumsum))
print(df.apply(np.exp))

# the apply() method will also dispatch on a string method name
print(df.apply('mean'))
print(df.apply('mean', axis=1))