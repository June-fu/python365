#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-09 21:37:10
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-09 21:37:14
 # @ Description:
Transforming with a dict
'''
import pandas as pd
import numpy as np

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('2000/1/1', periods=10))
print(tsdf)

# Passing a dict of functions will allow selective transforming per column
print(tsdf.transform({'A': np.abs, 'B': lambda x: x + 1}))

# Passing a dict of lists will generate a MultiIndexed DataFrame with these selective transforms
print(tsdf.transform({'A': np.abs, 'B': [lambda x: x + 1, 'sqrt']}))