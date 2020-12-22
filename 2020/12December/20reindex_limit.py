#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-17 22:58:34
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-17 22:58:36
 # @ Description:
 Limits on filling while reindexing
 '''

import pandas as pd
import numpy as np

rng = pd.date_range('1/3/2020', periods=8)
s = pd.Series(np.random.randn(8), index=rng)
print(s)

s2 = s[[0, 3, 6]]
print(s2)

# The linit and tolerance arguments provide additional control over filling while reindexing
print(s2.reindex(s.index, method="ffill", limit=1))

# in contrast, tolerance specifies the maximum distance between the index and indexer values
print(s2.reindex(s.index, method='ffill', tolerance='2 day'))