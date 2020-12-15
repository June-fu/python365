#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-15 23:11:33
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-15 23:12:08
 # @ Description:
Filling while reindexing
 '''

import pandas as pd
import numpy as np

# reindex() takes an optional parameter method which is a filling method chosen from the following table;
rng = pd.date_range('1/3/2020', periods=8)
s = pd.Series(np.random.randn(8), index=rng)
print(s)

s2 = s[[0, 3, 6]]
print(s2)

# pad/ffill Fill values forward
print(s2.reindex(s.index, method='pad'))
# bfill/backfill Fill values backward
print(s2.reindex(s.index, method='bfill'))
# nearest Fill from the nearest values
print(s2.reindex(s.index, method='nearest'))
# These methods require that the indexes are ordered increasing or decreasing;otherwise it will raise a ValueError
# but fillna() <except 'nearest'>and interpolate() will not
print(s2.reindex(s.index).fillna(method='ffill'))
print(s2.reindex(s.index).interpolate(method='nearest'))

