#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-02 23:31:51
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-02 23:31:56
 # @ Description:
Series has the nsmallest() and nlargest() methods which return the smallest or
largest n values.
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.random.permutation(10))
print(s)

print(s.sort_values())
print(s.nsmallest(3))
print(s.nlargest(3))

df = pd.DataFrame({
    'a': [-2, -1, 1, 10, 8, 11, -1],
    'b': list('abcdeff'),
    'c': [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0]
})
print(df.nlargest(3, 'a'))
print(df.nlargest(5, ['a', 'c']))
print(df.nsmallest(3, 'a'))
print(df.nsmallest(5, ['a', 'c']))