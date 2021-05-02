#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-05-03 00:06:36
 # @ Modified by: june-fu
 # @ Modified time: 2021-05-03 00:06:41
 # @ Description:
 '''

import pandas as pd
import numpy as np

dfj = pd.DataFrame(np.random.randn(5,2), columns=list('AB'))
print(dfj)
print(dfj.to_json())