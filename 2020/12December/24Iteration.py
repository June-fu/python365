#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-21 21:25:36
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-21 21:25:40
 # @ Description:
 basic iteration(for i in object) produces:
 Series: values
 DataFrame: column labels
 '''

import pandas as pd
import numpy as np

# DataFrame follow the dict-like convention of iterating over the "keys" of the objects
df = pd.DataFrame({'col1': np.random.randn(3),
                    'col2': np.random.randn(3)}, index=['a', 'b', 'c'])

for col in df:
    print(col)

# Pandas objects also have the dict-like items() method to iterate over the (key,value) pairs
# itertuples() is a lot faster than iterrows(), and is in most cases preferable to use to iterate over the vales of a DataFrame

# You should never modify something you are iterating over
df1 = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})

for index, row in df1.iterrows():
    row['a'] = 10 # this has no effect
print(df1)