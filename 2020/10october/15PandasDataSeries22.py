#!/usr/bin/pyton
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-03 22:02:22
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-03 22:02:27
 # @ Description:
 Write a Pandas program to extract items at given positions of a given series
 '''

import pandas as pd

s = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
print("Original Series:\n", s)
result = s.take(element_pos)
print("Extract items at given pisitions of the said Series:\n", result)