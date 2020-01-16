# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/16
"""
check Armstrong Number
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
实例：
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

"""


def is_armstrong(num):
    total_sum = 0
    for i in list(map(int, str(num))):
        total_sum += pow(i, len(str(num)))
    if total_sum == num:
        return True
    else:
        return False


if __name__ == '__main__':
    x = 153
    if is_armstrong(x):
        print("{} is an Armstrong number".format(x))
    else:
        print("{} is an Armstrong number".format(x))
