#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/14
"""
DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it
like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.
Like Series, DataFrame accepts many different kinds of input:
DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it
like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.
Like Series, DataFrame accepts many different kinds of input:
1. Dict of 1D ndarrays, lists, dicts, or Series
2. 2-D numpy.ndarray
3. Structured or record ndarray
4. A Series
5. Another DataFrame
"""

# From dict of Series or dicts
import numpy as np
import pandas as pd

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

print(pd.DataFrame(d, index=['d', 'b', 'a']))
print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))

# The row and column labels can be accessed respectively by accessing the index and columns attributes:
print(df.index)
print(df.columns)

