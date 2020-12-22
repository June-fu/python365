#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-13 23:03:13
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-13 23:03:31
 # @ Description:
 Write a Pandas program to replace missing white spaces in a given string with the least frequent character
 '''
import pandas as pd
import numpy as np

s = pd.Series(list('abc def abcdef icd'))
print("Original series:\n", s)
element_freq = s.value_counts()

current_freq = element_freq.dropna().index[-1]
print(''.join(s.replace(" ",current_freq)))