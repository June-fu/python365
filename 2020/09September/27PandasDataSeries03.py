#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-21 14:04:44
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-21 14:04:47
 # @ Description:
 Write a Pandas program to add, subtract, multiple and divide two Pandas Series
 '''

import pandas as pd

s1 = pd.Series([2, 4, 6, 8])
s2 = pd.Series([1, 3, 2 ,4])

print(s1 +  s2)
print(s1.add(s2))

print(s1.sub(s2))
print(s1.mul(s2))
print(s1.div(s2))