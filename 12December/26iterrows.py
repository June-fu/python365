#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-22 22:44:37
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-22 22:44:39
 # @ Description:
 iterrows() allows you to iterate through the rows of a DataFrame as Series objects
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': np.random.randn(3),
                    'col2': np.random.randn(3)}, index=['a', 'b', 'c'])
for row_index, row in df.iterrows():
    print(row_index, row, sep='\n')

# iterrows() does not preserve dtypes across the rows
df1 = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
print(df1.dtypes)

row = next(df1.iterrows())[1]
print(row)

print("in row, all values are upcasted to floats:", row['int'].dtype)
print("the original integer value:", df1['int'].dtype)
# To preserve dtypes whlile iterating the rows, it is better to use itertuples()

#a contrived way to transpose the DataFrame would be:
df2 = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df.T)

df2_t = pd.DataFrame({idx: values for idx ,values in df.iterrows()})
print("A contrived way:", df2_t, sep='\n')