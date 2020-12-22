#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-25 23:00:54
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-25 23:00:57
 # @ Description:
Make regex readable
 '''

import re
from functools import partial

norm_space = partial(re.sub, r'\s+', ' ')
print(norm_space(' a b\tc d'))