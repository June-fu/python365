#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-02-25 22:46:33
 # @ Modified by: june-fu
 # @ Modified time: 2021-02-25 22:46:58
 # @ Description:
 # Write a Pandas program to set a given value for particular cell in  DataFrame using index value
 '''

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("Original DataFrame:\n", df)

df['score'][8]= 10.2
print("Set a given value for particular cell in the DataFrame:\n", df)
