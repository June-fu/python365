#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-20 23:05:53
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-20 23:05:56
 # @ Description:
Write a Pandas program to select a row of series/dataframe by given integer index.
 '''

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("Original DataFrame:\n", df)

result = df.fillna(0)
print('Index-2: Details:\n', result)