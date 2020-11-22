#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Write a Pandas program to change the data type of a given column or Series
import pandas as pd

s = pd.Series([100, 200, 'python', 300.12, 400])
print(s)

print("Change the said data type to numeric")
s2 = pd.to_numeric(s, errors='coerce')
print(s2)