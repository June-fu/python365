#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/23
"""
From a Series
The result will be a DataFrame with the same index as the input Series,
and with one column whose name is the original name of the Series (only if no other column name provided).
"""
import pandas as pd
import numpy as np

s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'], name='hello')
print(s)

print(pd.DataFrame(s))
