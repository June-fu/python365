#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-11 22:24:07
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-11 22:24:10
 # @ Description:
reindexing and altering labels
reindex() accomplishes several things:
1. Recorder the existing data to match a new set of labels
2. Inserts missing value(NA) markers in label locations where no data for that label existed
3. if specified, fill data for missing labels using logic(highly relevant to working with time series data)
'''

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print("Reindex the Series:\n", s.reindex(['e', 'b', 'f', 'd']))

# with a DataFrame, you can simultaneously reindex the index and columns
df = pd.DataFrame(np.random.randn(4, 3), columns=['one', 'two', 'three'],
                index=['a', 'b', 'c', 'd'])
print(df)

print("DataFrame reindex:\n", df.reindex(index=['c', 'f', 'b'], columns=['three', 'two', 'one']))

# you can also use reindex with an axis keyword:
print(df.reindex(['c', 'f', 'b'], axis='index'))

# Note that the Index objects containing the actual axis labels can be shared between objects
rs = s.reindex(df.index)
print(rs)
print(rs.index is df.index)

# DataFrame.reindex() also supports an "axis-style" calling convention
print(df.reindex(['c', 'b', 'f'], axis='index'))
print(df.reindex(['three', 'two', 'one'], axis='columns'))