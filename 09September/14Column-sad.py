#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/23
"""
Column selection, addition, deletion
"""

import pandas as pd
import numpy as np

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

print(df)
print(df['one'])
df['three'] = df['one'] * df['two']

print(df)
df['flag'] = df['one'] > 2

print(df)

# Columns can be deleted or popped like with a dict:
del df['two']
print(df)

three = df.pop('three')
print(df)

# When inserting a scalar value, it will naturally be propagated to fill the column:
df['foo'] = 'bar'
print(df)

# When inserting a Series that does not have the same index as the DataFrame,
# it will be conformed to the DataFrame’s index:
df['one_trunc'] = df['one'][:2]
print(df)

# You can insert raw ndarrays but their length must match the length of the DataFrame’s index.
# By default, columns get inserted at the end.
# The insert function is available to insert at a particular location in the columns:
df.insert(1, 'bar', df['one'])
print(df)
