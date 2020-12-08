#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-08 23:04:27
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-08 23:04:39
 # @ Description:
 transform() method returns an object that is indexed the same(same size) as the original
 '''

import pandas as pd
import numpy as np

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2000', periods=10))

print(tsdf)
tsdf.iloc[3:7] = np.nan
print(tsdf)

# transform() allows input functions as: a Numpy function, a String function name or a user defined function
print(tsdf.transform(np.abs))
print(tsdf.transform('abs'))
print(tsdf.transform(lambda x: x.abs()))
# when received a single function, this is equivalent to ufunc application
print(np.abs(tsdf))

# Passing a single function to .transform() with a Series will yield a single Series in return.
print(tsdf['A'].transform(np.abs))