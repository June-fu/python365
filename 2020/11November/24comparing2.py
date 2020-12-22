#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-24 22:11:22
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-24 22:11:24
 # @ Description:
 comparing array-like objects
 '''
import pandas as pd
import numpy as np

# element-wise comparisons
# comparing a pandas data structure with a scalar value
print(pd.Series(['foo', 'bar', 'baz']) == 'foo')

print(pd.Index(['foo', 'bar', 'baz']) == 'foo')

# comparisons between different array-like objects of the same length
print(pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'baz']))
print(pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux']))

# compare Index or Series objects of different lengths will raise a ValueError
# print(pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo', 'bar']))

# but NumPy ,a comparsion can be broadcast
print(np.array([1, 2, 3]) == np.array([2]))

# or it can return False if broadcasting can not be done
print(np.array([1, 2, 3]) == np.array([1, 2]))