#!/usr/bin/python
# -*- conding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-06 21:43:18
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-06 21:43:20
 # @ Description:
Write a Pandas program convert the first and last character of each word to upper case in each word of a given series
'''

import pandas as pd

s = pd.Series(['php', 'python', 'java', 'c#'])
print("Original Series:\n", s)
result = s.map(lambda x: x.title()[:-1] + x[-1].upper())
print("First and last character of each word to upper case:\n", result)