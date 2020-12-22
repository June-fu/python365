#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/27
"""
Indexing / selection

"""
import pandas as pd

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

# Select column
# df[col]->Series
print(df['one'])
print(type(df['one']))

# Select row by label
# df.loc[label] Series
print(df.loc['a'])
print(type(df.loc['a']))

# Select row by integer location
# df.iloc[loc] -> Series
print(df.iloc[1])
print(type(df.iloc[1]))

# Slice rows
# df[5:10]->DataFrame
print(df[1:3])
print(type(df[1:3]))

# Select rows by boolean vector
# df[bool_vec]->DataFrame
print(df[df['one'] > 1])
