#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-26 23:45:13
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-26 23:45:18
 # @ Description:
  Write a Pandas program to change the order of index of a given series
 '''

import pandas as pd

s = pd.Series(data=[1,2,3,4,5], index=['A', 'B', 'C', 'D', 'E'])
print("Original Data Series:\n", s)

s = s.reindex(['B', 'A', 'C', 'D', 'E'])
print("Data Series after changing the order of index:\n", s)