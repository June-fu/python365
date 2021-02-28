#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-28 22:08:27
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-28 22:09:04
 # @ Description:
 Write a Pandas program to drop a list of rows from a specified DataFrame
 '''

import pandas as pd
import numpy as np

data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

print("New DataFrame after removing 2nd & 4th rows:\n", df.drop(df.index[[2, 4]]))
