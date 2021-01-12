#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-12 23:47:52
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-12 23:47:54
 # @ Description:
 Performing selection operations on integer type data can easily upcast the data to floating.
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': pd.Series(np.random.randn(8), dtype='float16'),
                   'B': pd.Series(np.random.randn(8)),
                   'C': pd.Series(np.array(np.random.randn(8),
                                           dtype='float64'))})
dfi = df.astype('int32')
print(dfi)
dfi['E'] = 1
print(dfi.dtypes)

casted = dfi[dfi > 0]
print(casted)
print(casted.dtypes) # column E are not change because nans are not introduced

# While float dtypes are unchanged.
dfa = df.copy()
dfa['A'] = dfa['A'].astype('float32')
print(dfa.dtypes)

casted = dfa[dfa > 0]
print(casted)
print(casted.dtypes)