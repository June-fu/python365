#!/usr/bin/python
'''
 # @ Author: june-fu
 # @ Create Time: 2021-03-07 23:50:39
 # @ Modified by: june-fu
 # @ Modified time: 2021-03-07 23:50:42
 # @ Description:
 The default NaN recognized values are ['-1.#IND', '1.#QNAN', '1.#IND', '-1.#QNAN', '#N/A N/A', '#N/A', 'N/A', 'n/a', 'NA', '<NA>', '#NA', 'NULL', 'null', 'NaN', '-NaN', 'nan', '-nan', '']
 '''

import pandas as pd

df = pd.read_csv("./data/new_file.csv", delimiter='\t')
print(df)

# specify a string in na_values.
df2 = pd.read_csv("./data/new_file.csv", delimiter="\t", na_values=[5])
print(df2)

# only an empty field will be recognized as NaN.
df3 = pd.read_csv("./data/new_file.csv", delimiter="\t", keep_default_na=False, na_values=[""])
print(df3)

# both NA and 0 as strings are NaN.
print(pd.read_csv("./data/new_file.csv", delimiter="\t", keep_default_na=False, na_values=["NA", "0"]))


# The default values, in addition to the string "Nope" are recognized as NaN.
print(pd.read_csv("./data/new_file.csv", delimiter="\t", na_values=["Nope"]))

