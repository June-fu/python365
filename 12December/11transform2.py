#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-09 21:28:47
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-09 21:28:48
 # @ Description:
 Transform with multiple functions
 '''

import pandas as pd
import numpy as np

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('2000/1/1', periods=10))
print(tsdf)

# passing multiple functions will yield a column MultiIndexed DataFrame.
print(tsdf.transform([np.abs, lambda x: x + 1]))

# Passing multiple functions to a Series will yield a DataFrame.
print(tsdf['A'].transform([np.abs, lambda x: x + 1]))