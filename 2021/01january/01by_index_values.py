#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-28 23:01:14
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-28 23:02:10
 # @ Description:
 '''

import pandas as pd
import numpy as np

idx = pd.MultiIndex.from_tuples(
    [('a', 1), ('a', 2), ('a', 2), ('b', 2), ('b', 1), ('b', 1)]
)
idx.names = ['first', 'second']
print(idx)

# Build DataFrame
df_multi = pd.DataFrame(
    {'A': np.arange(6, 0, -1)}, index=idx
)
print(df_multi)

# Sort by 'second'(index) and 'A' column
print(df_multi.sort_values(by=['second', 'A']))