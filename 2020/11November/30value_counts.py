#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-29 21:58:09
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-29 21:58:24
 # @ Description:
 The value_counts() Series method and top-level function computes a histogram of a 1D array of values
 '''

import pandas as pd
import numpy as np

data = np.random.randint(0, 7, size=50)
print(data)
s = pd.Series(data)
print(s.value_counts())

print(pd.value_counts(data))
