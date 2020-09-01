#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/1
"""
Series is dict-like
A Series is like a fixed-size dict in that you can get and set values by index label
"""
import numpy as np
import pandas as pd

s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])

s['e'] = 12
print(s)
print('e' in s)
print('f' in s)

# If a label is not contained, an exception is raised:
# print(s['f'])

# Using the get method, a missing label will return None or specified default:
print(s.get('f'))
print(s.get('f', np.nan))
