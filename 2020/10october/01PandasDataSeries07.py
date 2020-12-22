#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-22 13:06:17
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-22 13:06:33
 # @ Description:
 Write a Pandas program to convert the first column of a DataFrame as a Series
 '''

import pandas as pd

d = {'col1':[1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame:\n", df)

# convert the first column of df as a Series
s = df['col1']
print("Convert the first column as a Series:\n", s)
print(type(s))
