#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/9
"""
Series can also have a name attribute:
"""
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), name='haha')
print(s)
print(s.name)

# The Series name will be assigned automatically in many cases,
# in particular when taking 1D slices of DataFrame as you will see below.

# You can rename a Series with the pandas.Series.rename() method.
# Note that s and s2 refer to different objects.
s2 = s.rename('aabb')
print(s2)
