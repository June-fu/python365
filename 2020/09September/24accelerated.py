#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-18 22:08:56
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-18 22:40:24
 # @ Description: 
 # 1、numexpr: for accelerating certain numerical operations;numexpr uses multiple cores as well as smart chunking and caching to achieve large speedups.
 # 2、bottleneck: for accelerating certain types of nan evaluations. bottleneck uses specialized cython routines to achieve large speedups

 '''
import pandas as pd

# how to control
#!!These are both enabled to be used by default
pd.set_option('compute.use_bottleneck', False)
pd.set_option('compute.use_numexpr', False)
