#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-23 22:49:02
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-23 22:49:06
 # @ Description:
 Write a Pandas program to convert Series of lists to one Series
 '''

import pandas as pd

s = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])

print("Origial Series of list:\n", s)

# convert s to one Series
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series:\n", s)