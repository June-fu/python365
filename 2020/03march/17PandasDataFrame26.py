#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-26 21:40:30
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-26 21:40:42
 # @ Description:
Write a Pandas program to add one row in an existing DataFrame
 '''

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame", df, sep='\n')

d2 = {'col1': 10, 'col2': 11, 'col3': 12}
print('After add one row:', df.append(d2, ignore_index=True), sep='\n')
