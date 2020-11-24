#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-24 22:11:22
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-24 22:11:24
 # @ Description:
Write a Pandas program to sort a given Series
 '''
import pandas as pd
import numpy as np

s = pd.Series(['100', '200', 'python', '300.12', '400'])
print('Original Data Series:\n', s)
print("Sorted Series:\n", s.sort_values())