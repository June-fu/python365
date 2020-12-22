#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/27
"""
Transposing
To transpose, access the T attribute (also the transpose function), similar to an ndarray:
"""
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2020', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index)
print(df)
print(df.T)

# only show the first 5 rows
print(df[:5].T)