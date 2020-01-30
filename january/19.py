#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/30
"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

# 看到这个问题，思路是除了二月份每年不一样，其余月份的天数是固定的；因此每月天数可以存入一个list或tuple中
# 二月份天数的确定需要用到判断闰年的程序；核心逻辑：四年一闰，百年不闰；四百年再闰。
def day_of_year(ymd):
    str1 = ymd
    list_str = str1.split('-')
    y = int(list_str[0])
    m = int(list_str[1])
    d = int(list_str[2])

    dom = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if m < 0 or m > 12:
        print("it is the wrong date!")
    days = dom[m - 1] + d
    if m > 2:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            days += 1
    return days


if __name__ == '__main__':
    x = input('请输入日期（yyyy-mm-dd)：')
    doy = day_of_year(x)
    print('%s 是这一年的第%d天' % (x, doy))
