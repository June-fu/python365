#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-22 12:53:39
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-22 12:53:50
 # @ Description:
 Write a Pandas program to convert a NumPy array to a Pandas series
 '''
import pandas as pd
import numpy as np

arr1 = np.arange(10, 60, 10)
print("Numpy array:", arr1)

print("Converted Pandas Series:\n", pd.Series(arr1))