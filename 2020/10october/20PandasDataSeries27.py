#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-08 23:14:50
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-08 23:14:53
 # @ Description:
 26 Write a Pandas program to compute difference of differences between consecutive numbers of a given series
 '''

import pandas as pd

s = pd.Series([1, 3, 5, 8, 10, 11, 15])
print("Original Series:\n", s)

print("Difference of differences between consecutive numbers of the said series:")
print(s.diff().to_list())
print(s.diff().diff().to_list())