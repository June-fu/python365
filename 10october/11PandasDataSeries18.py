#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-29 21:58:09
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-29 21:58:24
 # @ Description:
Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series
 '''

import pandas as pd
import numpy as np

num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10, 4, 20))

print("Original Series:\n", num_series)
result = np.percentile(num_series, q=[0, 25, 50, 75, 100])
print("Minimum, 25th percentile, median, 75th, and maximum of a given series:\n", result)