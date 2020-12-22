#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/27
"""
Data alignment and arithmetic
"""
# When doing an operation between DataFrame and Series,
# the default behavior is to align the Series index on the DataFrame columns, thus broadcasting row-wise
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print(df + df2)
print(df - df.iloc[0])

# In the special case of working with time series data,
# if the DataFrame index contains dates, the broadcasting will be column-wise
index = pd.date_range('1/1/2000', periods=8)
df3 = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
print(df3)
print(df3 - df3['A'])
print(df.sub(df['A'], axis=0))
