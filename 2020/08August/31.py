#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/8/30
"""
The basic method to create a Series is to call:

>> s = pd.Series(data, index=index)
Here, data can be many different things:
a Python dict
an ndarray
a scalar value (like 5)
"""
import numpy as np
import pandas as pd

# From ndarray
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(pd.Series(np.random.randn(5)))


# From dict
d = {'b': 1, 'a': 0, 'c': 2}
print(pd.Series(d))
print(pd.Series(d, index=['a', 'b', 'c', 'd']))

# From Scalar value
print(pd.Series(5, index=['a', 'b', 'c', 'd', 'e']))
