#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-28 23:12:32
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-28 23:12:35
 # @ Description:
Write a Pandas program to delete DataFrame row(s) based on given column value
 '''
import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame:", df, sep='\n')

df = df[df.col2 != 5]
print(df)