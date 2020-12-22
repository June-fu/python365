#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/23
"""
DataFrame.from_dict
takes a dict of dicts or a dict of array-like sequences and returns a DataFrame
"""

import pandas as pd

d = dict([('A', [1, 2, 3]), ('B', [4, 5, 6])])
print(d)

print(pd.DataFrame.from_dict(d))

# If you pass orient='index', the keys will be the row labels. In this case, you can also pass the desired column names
print(pd.DataFrame.from_dict(d, orient='index', columns=['one', 'two', 'three']))
