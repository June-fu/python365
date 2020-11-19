#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-19 22:42:52
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-19 22:43:14
 # @ Description:an elegant way to deal with file path
 '''

from pathlib import Path
data_folder = Path("data/")

# Path calculation and matadata
file_to_open = data_folder / "iris.txt"
print(file_to_open.name)
print(file_to_open.stem)

# Files functions
f = open(file_to_open)
print(f.read())
print(file_to_open.exists())