#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-26 20:51:20
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-26 20:51:26
 # @ Description:
 sort_values() method
 DataFrame.sort_values() method is used to sort a DataFrame by its column or row values
 '''
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
                'one': [2, 1, 1, 1],
                'two': [1, 3, 2, 4],
                'three': [5, 4, 3, 2]
})

print(df1.sort_values(by='two'))

# The by parameter can take a list of column names
print(df1.sort_values(by=['one', 'two']))

# These methods have special treatment of NA values via the na_position argument
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'],
              dtype="string")
print(s)
s[2] = np.nan
print(s.sort_values())
print(s.sort_values(na_position='first'))