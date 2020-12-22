#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Write a Pandas program to convert a given Series to an array
import pandas as pd
import numpy as np

s = pd.Series([100, 200, 'python', 300.12, 400])
print("Original Data Series:", s)

print("Series to an array:\n", np.array(s.values))
