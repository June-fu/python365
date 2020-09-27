#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/27
"""
Head and tail
"""
import pandas as pd
import numpy as np

long_series = pd.Series(np.random.randn(1000))
print(long_series.head())
print(long_series.tail())
