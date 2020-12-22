#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-13 23:03:22
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-14 22:27:37
 # @ Description:
 Write a Pandas program to compute the autocorrelations of a given numeric series
 '''
import pandas as pd
import numpy as np

s = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))
print("Original Series:\n", s)

autocorrelations = [s.autocorr(i).round(2) for i in range(11)]
print("Autocorrelations of the said Series:\n", autocorrelations[1:])