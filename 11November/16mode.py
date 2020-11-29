#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-29 21:58:09
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-29 21:58:24
 # @ Description:
get the most frequently occurring value
 '''

import pandas as pd
import numpy as np
s = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
print(s.mode())
df = pd.DataFrame({
    "A": np.random.randint(0, 7, size=50),
    "B": np.random.randint(-10, 15, size=50)
})
print(df)
print(df.mode())