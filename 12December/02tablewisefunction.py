#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
 # @ Author: june-fu
 # @ Create Time: 2020-11-30 22:12:42
 # @ Modified by: june-fu
 # @ Modified time: 2020-11-30 22:12:45
 # @ Description:
 DataFrame and Series can be passed into functions.
 if the function needs to be called in a chain ,consder using the pipe() method
 '''
import pandas as pd
import numpy as np

def extract_city_name(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df['city_name'] = df['city_and_code'].str.split(",").str.get(0)
    return df

def add_country_name(df, country_name=None):
    """
    Chicago -> Chicago-US for city_name column
    """
    col = 'city_name'
    df['city_and_country'] = df[col] + country_name
    return df

df_p = pd.DataFrame({'city_and_code': ['Chicago, IL']})
print(df_p)
print(add_country_name(extract_city_name(df_p), country_name='US'))

# It is equivalent to:
print(df_p.pipe(extract_city_name).pipe(add_country_name, country_name='US'))
# this is method chaining. and the functions expected a DataFrame as the first positional argument.