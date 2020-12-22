#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-17 23:06:34
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-17 23:13:56
 # @ Description:
Write a Pandas program to stack two given series vertically and horizontally.
 '''

import pandas as pd
import numpy as np

s1 = pd.Series(range(10))
s2 = pd.Series(list('pqrstuvwxy'))

print("Original Series:\n", s1, s2)
#print(s1.append(s2))

df = pd.concat([s1, s2], axis=1)
print(df)