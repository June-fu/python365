#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-03 21:53:15
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-03 21:53:54
 # @ Description:
 Aggregation with a single function
 '''
import pandas as pd
import numpy as np

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2020', periods=10))
print(tsdf)

tsdf.iloc[3:7] = np.nan
print(tsdf)

# using a single function is equivalent to apply().
print(tsdf.agg(np.sum))
# these are equivalent to a "sum()" because we are aggregating on a single function
print(tsdf.agg('sum'))
print(tsdf.sum())

# Single aggregations on a Series this will return a scalar value
print(tsdf['A'].agg('sum'))