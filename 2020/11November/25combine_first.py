#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-25 23:00:54
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-25 23:00:57
 # @ Description:
  combine two DataFrame objects where missing values in one DataFrame are conditionally filled with like-labeled values from the other DataFrame
 '''

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1., np.nan, 3., 5., np.nan],
                    'B': [np.nan, 2., 3., np.nan, 6.]})
df2 = pd.DataFrame({'A': [5., 2., 4., np.nan, 3., 7.],
                    'B': [np.nan, np.nan, 3., 4., 6., 8.]})

print(df1.combine_first(df2))