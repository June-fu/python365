#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-06 22:18:34
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-07 22:00:56
 # @ Description:
with .agg() it is possible to easily create a custom describe function
 '''
import pandas as pd
import numpy as np
from functools import partial

tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2020', periods=10))
print(tsdf)

q_25 = partial(pd.Series.quantile, q=0.25)
q_25.__name__ = '25%'
q_75 = partial(pd.Series.quantile, q=0.75)
q_75.__name__ = '75%'

print(tsdf.agg(['count', 'mean', 'std', 'min', q_25, 'median', q_75, 'max']))