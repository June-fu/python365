#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/23
"""
DataFrame.from_records takes a list of tuples or an ndarray with structured dtype
"""
import numpy as np
import pandas as pd

data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
print(data)
# DataFrame index may be a specific field of the structured dtype
print(pd.DataFrame.from_records(data, index='C'))
