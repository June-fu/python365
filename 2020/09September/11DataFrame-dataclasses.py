#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/9/23
"""
From a list of dataclasses
Data Classes can be passed into  the DataFrame constructor.Passing a list of dataclasses is equivalent to
passing a list of dictionaries.
Please be aware that all values in the list should be dataclasses, mixing types in the lists would result in a TypeError.
"""
import pandas as pd
import numpy as np
from dataclasses import make_dataclass
# New in version 1.1.0.
Point = make_dataclass("Point", [("x", int), ("y", int)])
df = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])

print(df)
