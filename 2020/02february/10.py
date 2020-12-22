#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/8
"""
1、select * from company where title like "%abc%" or mecount>999 order by createtime desc;

2、两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
"""


def sql_to_python():
    company = [{'title': 'ssabcdd', 'mecount': 123, 'createtime': '2020-12-01'},
               {'title': 'ssabcdd', 'mecount': 1000, 'createtime': '2020-02-01'}]
    result = []
    for row in company:
        if row['title'].__contains__('abc') or row['mecount'] > 999:
            result.append(row)
    # from operator import itemgetter
    # result.sort(key=itemgetter('createtime'))
    result.sort(key=lambda x: x['createtime'])
    print(result)


def matrix():
    x = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(x)):
        for j in range(len(x[i])):
            result[i][j] = x[i][j] + y[i][j]
    print(result)


if __name__ == '__main__':
    sql_to_python()
    matrix()
