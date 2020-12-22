#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/7
"""
Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file.
The prigram should take two arguments.
The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
"""


def csv2xls(csv, excel):
    import tablib
    data = tablib.Dataset()

    with open(csv) as f:
        for line in f.readlines():
            data.append(line.split(','))
    with open(excel, 'wb') as f:
        f.write(data.export('xlsx'))


if __name__ == '__main__':
    c_name = '../february/a.csv'
    e_name = 'a.xlsx'

    csv2xls(c_name, e_name)

