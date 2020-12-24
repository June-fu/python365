#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-24 22:42:17
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-24 22:42:48
 # @ Description:
rename columns of a given DataFrame
 '''

import pandas as pd
import numpy as np

dct1 = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

df = pd.DataFrame(data=dct1)
print(df)
print(df.columns)

#df.colums = ['Column1', 'Column2', 'Column3']
df = df.rename(columns={'col1': 'Column1', 'col2': 'Column2', 'col3': 'Column3'})
print(df)