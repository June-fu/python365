#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-26 21:40:30
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-26 21:40:42
 # @ Description:
Write a Pandas program to write a DataFrame to CSV file using tab separator
 '''

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame", df, sep='\n')

print('Data from new_file.csv file:')
df.to_csv('./data/new_file.csv', sep='\t', index=False)
print(pd.read_csv('./data/new_file.csv'))