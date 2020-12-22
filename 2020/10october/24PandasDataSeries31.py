#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-11 23:12:52
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-11 23:12:56
 # @ Description:
 Write a Pandas program to compute the Euclidean distance between two given series.
 '''
import pandas as pd
import numpy as np

x = pd.Series([1,2,3,4,5,6,7,8,9,10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:\n", x, y)
print("Euclidean distance between two said series:\n", np.linalg.norm(x - y))