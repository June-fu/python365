#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-27 22:16:47
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-27 22:16:52
 # @ Description:
 Write a Pandas program to get the items of a given series not present in another given series
 '''

import pandas as pd

s1 = pd.Series(data=[1, 2, 3, 4, 5])
s2 = pd.Series(data=[2, 4, 6, 8, 10])
print("Original Series:\n", s1)
print(s2)

print("Items of s1 not present in s2:\n", s1[~s1.isin(s2)])