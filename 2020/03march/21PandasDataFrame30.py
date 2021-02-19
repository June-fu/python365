#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-19 22:17:05
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-19 22:17:19
 # @ Description:
 Write a Pandas program to widen output display to see more columns
 '''

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)

print(df)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print("original DataFrame")
print(df)