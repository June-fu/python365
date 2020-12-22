#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-21 16:03:25
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-21 16:03:40
 # @ Description:
 Write a Pandas program to compare the elements of the two Pandas Series
 '''
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

print("Series1:\n", ds1)
print("Series2:\n", ds2)

print("Compare the elements of the said Series:")
print("Equals:\n", ds1 == ds2)
print("Greater than:\n", ds1> ds2)
print("Less than:\n", ds1<ds2)