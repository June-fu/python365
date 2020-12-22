#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/7
"""
求一个3 * 3矩阵主对角线元素之和
"""


class FontColor:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def matrix_diagonal_sum(num):
    a = []
    total = 0
    for i in range(num):
        a.append([])
        for j in range(num):
            a[i].append(int(input("Please input a integer number:")))
            if i == j:
                total += a[i][j]
    return total


if __name__ == '__main__':
    print(FontColor.GREEN + str(matrix_diagonal_sum(3)) + FontColor.END)

