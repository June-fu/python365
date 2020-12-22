#!/usr/bin/python
# -*- conding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-06 21:43:18
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-06 21:43:20
 # @ Description:
 when presented with mixed dtypes that cannot aggregate,
 .agg will only take the valid aggregations
 '''

import pandas as pd

mdf = pd.DataFrame({'A': [1, 2, 3],
                    'B': [1., 2., 3.],
                    'C':['foo', 'bar', 'baz'],
                    'D': pd.date_range('20130101', periods=3)})
print(mdf)

print(mdf.agg(['min', 'sum']))