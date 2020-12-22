#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/30
"""
to_numpy() gives some control over the dtype of the resulting numpy.ndarray.

there are two possibly useful representations:
1、An object-dtype numpy.ndarray with Timestamp objects, each with the correct tz

2、A datetime64[ns] -dtype numpy.ndarray, where the values have been converted to UTC and the timezone discarded
"""
import pandas as pd
import numpy as np

ser = pd.Series(pd.date_range('2000', periods=2, tz='CET'))
# Timezones may be preserved with dtype=object
print(ser.to_numpy(dtype=object))

# Or thrown away with dtype='datetime64[ns]'
print(ser.to_numpy(dtype="datetime64[ns]"))


index = pd.date_range('1/1/2020', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index)
# When your DataFrame only has a single data type for all the columns,
# DataFrame.to_numpy() will return the underlying data:

print(df.to_numpy())