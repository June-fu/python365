#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/9
"""
矩阵最小路径和
给定一个矩阵，大小为m，从左上角开始每次只能向右走或者向下走，最后达到右下角的位置。路径中所有数字累加起来就是路径和，返回所有路径的最小路径和。
实例：
4 1 5 3
3 2 7 7
6 5 2 8
8 9 4 5

23
"""


def min_matrix_path(m):
    lst = [[4, 1, 5, 3],
           [3, 2, 7, 7],
           [6, 5, 2, 8],
           [8, 9, 4, 5]]
    path_sum = lst[0][0]
    i = 0
    j = 0
    for x in range(2 * (m - 1)):
        if i == m - 1 and j == m - 1:
            break
        elif j + 1 >= len(lst[i]) and i + 1 < len(lst):
            path_sum += lst[i + 1][j]
            i += 1
        elif i + 1 >= len(lst) and j + 1 < len(lst[i]):
            path_sum += lst[i][j + 1]
            j += 1
        elif lst[i][j + 1] >= lst[i + 1][j]:
            path_sum += lst[i + 1][j]
            i += 1
        elif lst[i][j + 1] < lst[i + 1][j]:
            path_sum += lst[i][j + 1]
            j += 1

    print(path_sum)


if __name__ == '__main__':
    min_matrix_path(4)

