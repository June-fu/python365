#/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-04 22:55:24
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-04 22:55:53
 # @ Description:
 You can pass multiple aggregation arguments as a list. 
 The results of each of the passed functions will be a row in the resulting DataFrame. 
 '''

import pandas as pd
import numpy as np

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2020', periods=10))
print(tsdf)

# Aggrating with multiple functions
print(tsdf.agg(['sum']))
# multiple functions yield multiple rows
print(tsdf.agg(['sum', 'mean']))

# on a Series,mlutiple functions return a Series ,indexed by the function names
print(tsdf['A'].agg(['sum', 'mean']))

# what if pass a lambda function? <lambda>
print(tsdf['A'].agg(['sum', lambda x: x.mean()]))