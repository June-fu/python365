#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/9
"""
打印出杨辉三角形（要求打印出10行）
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
"""


def yh_triangle(num):
    triangle = []
    for i in range(num):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i+1):
            if j == i:
                triangle[i].append(1)
                break
            else:
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        print(' '.join(str(x) for x in triangle[i]))


if __name__ == '__main__':
    yh_triangle(10)
