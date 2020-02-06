#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/6
"""
输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
"""


# .一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
def is_palindrome(num):
    lst = str(num)
    length = len(lst)
    for i in range(int(length/2)):
        if lst[i] == lst[- i - 1]:
            continue
        else:
            return False
    return True


# 输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
def day_of_week():
    s1 = input("please input the first letter:")
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    lst = [x for x in week if x.lower().startswith(s1.lower())]
    while len(lst) > 1:
        s = input("please input the next letter:")
        s1 += s
        lst = [x for x in week if x.lower().startswith(s1.lower())]

    if not lst:
        print('please input the right letter!')
        dow = day_of_week()
        lst = [dow]
    return lst[0]


if __name__ == '__main__':
    print(is_palindrome(12321))
    print(day_of_week())



