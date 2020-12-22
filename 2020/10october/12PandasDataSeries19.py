#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-30 22:37:15
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-30 22:38:13
 # @ Description:
 Write a Pandas program to calculate the frequency counts of each unique value of a given series.
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
print("Original Series:\n", s)
result = s.value_counts()
print("Frequency of each unique value of the Said series:\n", result)
