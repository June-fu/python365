#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-12 23:36:41
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-12 23:36:45
 # @ Description:
 Write a Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series
 '''
import pandas as pd
import numpy as np

s = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:\n", s)

result = []
for i in range(1, len(s)-1):
    if s[i] > s[i-1] and s[i] > s[i+1]:
        result.append(i)
print(result)

# the second method, use diff()    
temp = np.diff(np.sign(np.diff(s)))
print(np.where(temp == -2)[0] + 1)