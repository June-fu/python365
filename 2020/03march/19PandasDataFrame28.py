#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-28 23:12:32
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-28 23:12:35
 # @ Description:
 Write a Pandas program to count city wise number of people from a given of data set
 '''
import pandas as pd

df = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
print(df)

print(df.groupby(['city']).size().reset_index(name='Number of people'))