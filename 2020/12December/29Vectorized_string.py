#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-26 12:13:08
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-26 12:13:13
 # @ Description:
Series's str attribute
 '''

import pandas as pd
import numpy as np

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'], dtype="string")
print(s.str.lower())

# Pandas supports three kinds of sorting: 
# sorting by index labels
df = pd.DataFrame({
             'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
             'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
             'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
print(df)
unsort_df = df.reindex(index=['a', 'd', 'c', 'b'],
                        columns=['three', 'two', 'one'])
print(unsort_df)

# DataFrame.sort_index()
print(unsort_df.sort_index())
print(unsort_df.sort_index(ascending=False))
print(unsort_df.sort_index(axis=1))
print(unsort_df['three'].sort_index())
