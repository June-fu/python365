#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-22 12:53:39
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-22 12:53:50
 # @ Description:
 Write a Pandas program to convert a dictionary to a Pandas series
 '''

import pandas as pd

dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print("Original dictionary:", dict1)

print("Converted Series:\n", pd.Series(dict1))