#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/22
"""
From structured or record array
identically to a dict of arrays.
"""
import pandas as pd
import numpy as np

d = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
print(d)
d[:] = [(1, 2., 'Hello'), (2, 3., 'World')]
print(pd.DataFrame(d))

print(pd.DataFrame(d, index=['first', 'second']))
print(pd.DataFrame(d, columns=['C', 'B', 'A']))

