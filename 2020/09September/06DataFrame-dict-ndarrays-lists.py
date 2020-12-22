#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/14
"""
From dict of ndarrays / lists
The ndarrays must all be the same length
 If an index is passed, it must clearly also be the same length as the arrays.
 If no index is passed, the result will be range(n), where n is the array length.
"""

import pandas as pd
d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
print(pd.DataFrame(d))
print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))
