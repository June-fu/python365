#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-13 22:53:42
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-13 22:53:45
 # @ Description:
 The align() method is the fastest way to simultaneously align two objects.
It supports a join argument.it returns a tuple with both of the reindexed Series:
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

s1 = s[:4]
s2 = s[1:]

# join='outer': take the union of the indexes (default)
print(s1.align(s2))

# join='inner': intersect the indexes
print(s1.align(s2, join='inner'))
# join='left': use the calling object's index
print(s1.align(s2, join='left'))
# join='right': use the passed object's index
print(s1.align(s2, join='right'))