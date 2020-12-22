#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-06 22:03:48
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-06 22:03:52
 # @ Description:
 Write a Pandas program to calculate the number of characters in each word in a given series.
 '''

import pandas as pd

s = pd.Series(['php', 'python', 'java', 'c#'])
print("Original Series:\n", s)
result = s.map(lambda x: len(x))
print("Number of characters in each word in the said series:\n", result)