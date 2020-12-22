#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-02 22:48:20
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-02 22:48:25
 # @ Description:
 Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series. 
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(1, 10, 9))
print("Original Series:\n", s)
result = s[s.values % 5 == 0].index.values
print("Positions of numbers that are multiples of 5:\n", result)
result2 = np.argwhere(s.values % 5 == 0)
print(result2)