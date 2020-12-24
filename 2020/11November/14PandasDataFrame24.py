#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-24 22:42:17
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-24 22:42:48
 # @ Description:
select rows from a given DataFrame based on values in some columns
 '''

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame:", df, sep='\n')

print('Rows for colum1 value == 4:', df.loc[df['col1'] == 4], sep='\n')