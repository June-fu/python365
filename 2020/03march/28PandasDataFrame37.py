#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-10 22:08:27
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-10 22:09:04
 # @ Description:
 Write a Pandas program to reset index in a given DataFrame.
 '''

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("Original DataFrame:\n", df)

df2 = df.drop([0, 1])
print("\nAfter removing first and second rows:\n", df2)
print("\nReset the Index:\n", df2.reset_index())