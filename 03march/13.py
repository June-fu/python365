#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/4/2
"""
Amortize problem
# 20万贷款，分期3年，按月还款，年利率4.65%，每月还款2000，最后一次还款多少？

functools.reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from left to right,
so as to reduce the iterable to a single value.
"""


# using functools.reduce()
def last_payment(total, month_pay, rate, year):
    from itertools import repeat
    from functools import reduce
    month_payment = [e for e in repeat(- month_pay, year * 12)]
    print(reduce(lambda x, y: x * (1 + rate / 100 / 12) + y, [total] + month_payment))


if __name__ == '__main__':
    last_payment(200000, 2000, 4.65, 3)