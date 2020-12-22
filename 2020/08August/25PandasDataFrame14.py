#!/usr/bin/pyton
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-20 22:29:41
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-20 22:29:56
 # @ Description:
 calculate the mean score for each different student in DataFrame.
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

print(df['score'].mean())