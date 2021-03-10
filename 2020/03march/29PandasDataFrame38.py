#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-10 22:16:03
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-10 22:17:09
 # @ Description:Write a Pandas program to divide a DataFrame in a given ratio.
 '''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2))
print("Original DataFrame:\n", df)

part_70 = df.sample(frac=0.7, random_state=10)
part_30 = df.drop(part_70.index)
print("\n70% of the said DataFrame:\n", part_70)
print("\n30% of the said DataFrame:\n", part_30)