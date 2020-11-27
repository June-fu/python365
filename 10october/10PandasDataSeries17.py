#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-27 22:16:47
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-27 22:16:52
 # @ Description:
 Write a Pandas program to get the items which are not common of two given Series
 '''

import pandas as pd
import numpy as np

s1 = pd.Series(data=[1, 2, 3, 4, 5])
s2 = pd.Series(data=[2, 4, 6, 8, 10])
print("Original Series:\n", s1)
print(s2)

print("\nItems of a given series not present in another given series:")
sr1 = pd.Series(np.union1d(s1, s2))
sr2 = pd.Series(np.intersect1d(s1, s2))

print(sr1[~sr1.isin(sr2)])