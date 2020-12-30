#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-30 23:46:32
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-30 23:46:36
 # @ Description:
Series has the searchsorted() method, which works similarly to numpy.ndarray.searchsorted()
'''

import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3])
print(s.searchsorted([0, 3]))

# Find indices where elements should be inserted to maintain order.
print(s.searchsorted([0, 4]))
print(s.searchsorted([1, 3], side='right'))
print(s.searchsorted([1, 3], side='left'))

s2 = pd.Series([3, 1, 2])
print(s2.searchsorted([0, 3], sorter=np.argsort(s)))