#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/2
"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""


def is_prime2(num):
    for i in range(2, num):
        if not (num % i):
            return False
    return True


def factorization(num):
    if num < 2:
        print('This number should be a positive integer greater than one!')
        return
    elif is_prime2(num):
        print("This number must be composite!")
        return
    else:
        lst = [x for x in range(2, num) if is_prime2(x)]
        str1 = ''
        while int(num) != 1:
            for i in lst:
                if not num % i:
                    str1 += str(i) + '*'
                    num /= i
    return '*'.join(sorted(str1[:-1].split('*')))


if __name__ == '__main__':
    print(factorization(90))
