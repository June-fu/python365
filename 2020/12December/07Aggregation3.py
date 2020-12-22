#!/usr/bin/python
# -*- conding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-06 21:43:18
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-06 21:43:20
 # @ Description:
 Aggregating with a dict
 '''

import pandas as pd
import numpy as np

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2020', periods=10))
print(tsdf)

# customize which functions are applied to which columns
print(tsdf.agg({'A': 'mean', 'B': 'sum'}))

# passing a list-like will generate a DataFrame output
print(tsdf.agg({'A': ['mean', 'min'], 'B': 'sum'}))