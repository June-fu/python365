#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 21:37:46
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-20 21:38:50
 # @ Description:
select the specified columns and rows from a given data frame
'''
import pandas as pd
import numpy as np

dct1 = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(dct1, index=labels)
print(df)

print("Select specific columns and rows:\n", df.iloc[[1, 3, 5, 6], [1, 3]])