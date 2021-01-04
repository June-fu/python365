#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-04 22:39:18
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-04 22:39:20
 # @ Description:
 When trying to convert a subset of columns to a specified type using astype() and loc(), upcasting occurs.
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
})
print(df.dtypes)
print(df.loc[:, ['a', 'b']].astype(np.uint8).dtypes)

#  the following piece of code produces the unintended result.
df.loc[:, ['a', 'b']] = df.loc[:, ['a', 'b']].astype(np.uint8)
print(df.dtypes)