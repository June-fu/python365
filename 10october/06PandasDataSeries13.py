#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-25 23:00:54
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-25 23:00:57
 # @ Description:
 Write a Pandas program to create a subset of a given series based on value and condition
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.arange(11))
print("Original Series:\n", s)

print("Subset of the above Data Series:\n", s[s<6])