#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-04 23:05:13
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-04 23:05:16
 # @ Description:
 Write a Pandas program to get the positions of items of a given series in another given series. 
 '''

import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original Series:\n", s)

s2 = pd.Series([1, 3, 5, 7])
result = [pd.Index(s).get_loc(i) for i in s2]
print("Position if items of s2 in s is:\n", result)