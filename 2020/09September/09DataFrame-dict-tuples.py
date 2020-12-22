#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/22
"""
From a dict of tuples
You can automatically create a MultiIndexed frame by passing a tuples dictionary.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                  ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                  ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                  ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                  ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
print(df)
