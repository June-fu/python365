#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-21 21:25:36
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-21 21:25:40
 # @ Description:
 items() iterates through key-value pairs:
 Series: (index, scalar value) values
 DataFrame: (column,Series) pairs
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})

for label, ser in df.items():
    print("label:", label)
    print("Series:", ser)