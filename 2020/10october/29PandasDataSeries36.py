#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-17 23:06:22
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-17 23:06:50
 # @ Description:
 Write a Pandas program to convert given series into a dataframe 
 with its index as another column on the dataframe
 '''

import pandas as pd
import numpy as np

lst = list('ABCDEFGHIGKLMNOP')
num_arr = np.arange(8)
num_dict = dict(zip(num_arr, lst))

s = pd.Series(num_dict)

print(s)

df = s.to_frame().reset_index()
print(df.head())