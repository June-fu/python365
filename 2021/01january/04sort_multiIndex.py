#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-01-02 23:42:31
 # @ Modified by: june-fu
 # @ Modified time: 2021-01-02 23:42:34
 # @ Description:Sorting by a MultiIndex column
You must be explicit about sorting when the column is a MultiIndex , and fully specify all levels to by

 '''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3))
print(df)

df.columns = pd.MultiIndex.from_tuples(
    [('a', 'one'), ('a', 'two'), ('b', 'three')]
)


print(df.sort_values(by=('a', 'two')))