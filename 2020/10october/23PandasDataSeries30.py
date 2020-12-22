#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2020-12-10 23:25:32
 # @ Modified by: june-fu
 # @ Modified time: 2020-12-10 23:25:49
 # @ Description:
 Write a Pandas program to filter words from a given series that contain atleast two vowels
 '''

import pandas as pd
from collections import Counter

color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
print("Original Series:\n", color_series)

result = color_series.map(lambda  c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)

print("Filtered Words:\n", color_series[result])