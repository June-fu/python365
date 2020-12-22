#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-01 23:17:23
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-01 23:17:27
 # @ Description:
 Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series
 '''
import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(1, 5, [15]))
print("Original Series:\n", s)
print(s.value_counts().index[:1])

s[~s.isin(s.value_counts().index[:1])] = 'Other'
print(s)
