#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-22 23:00:54
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-22 23:00:57
 # @ Description:
 The itertuples() method will return an iterator yielding a namedtuple for each row in the DataFrame.
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': np.random.randn(3),
                    'col2': np.random.randn(3)}, index=['a', 'b', 'c'])

# the first element of the tuple will be the row's corresponding index value
# while the remaining values are the row values
for row in df.itertuples():
    print(row)

# this method does not convert the row to a Series object;
# it merely returns the values inside a namedtuple.
# therefore itertuples() preserves the data type of the values and is generally faster than iterrow()
