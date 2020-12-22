#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-02 22:33:19
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-02 22:33:23
 # @ Description:
 apply() combined with some cleverness can be used to answer many questions about a data set
 '''
import pandas as pd
import numpy as np

# we wanted to extract the date where the maximum value for each column occurred
tsdf = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2000', periods=1000))
print(tsdf)

print(tsdf.apply(lambda x: x.idxmax()))

# you may also pass additional arguments and keyword arguments to the apply() method
def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide

print(tsdf.apply(subtract_and_divide, args=(5,), divide=3))

# pass Series methods to carry out some Series operation on each column or row
print(tsdf.apply(pd.Series.interpolate))