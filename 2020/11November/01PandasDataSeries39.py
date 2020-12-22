#!/usr/bin/pyton
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-17 23:22:42
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-19 23:04:07
 # @ Description:
Write a Pandas program to find the index of the first occurrence of 
the smallest and largest value of a given series.
 '''

import pandas as pd

s = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("Original Series:\n", s)

print("Index of the first occurrence of the smallest and largest value of the said series:\n", s.idxmin(), s.idxmax())