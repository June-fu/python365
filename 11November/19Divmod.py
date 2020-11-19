#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-19 21:19:26
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-19 21:19:32
 # @ Description:Series and Index also support the divmod() builtin
 # This function takes the floor division and modulo operation at the same time returning a two-tuple of the same type as the left hand side
 '''

import pandas as pd
import numpy as np

s = pd.Series(np.arange(10))
print(s)
div, rem = divmod(s, 3)
print(div, rem)

idx = pd.Index(np.arange(10))
print(idx)
div2, rem2 = divmod(idx, 3)
print(div2, rem2)

#We can also do elementwise divmod()
div3, rem3 = divmod(s, [2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
print(div3, rem3)