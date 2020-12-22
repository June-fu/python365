#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/25
"""
Problem 9: Write a regular expression to validate a phone number.
"""


def validate_phone(num):
    import re

    # 目前开放的号段 130-139,145-149,150-159,160-169,170-179,180-189,190-199
    if re.fullmatch(r'^1(([3,5-9]\d{9})|(4[5-9]\d{8}))$', num):
        return True
    else:
        return False


if __name__ == '__main__':
    n = '13704328964'
    m = '14004328964'
    print(validate_phone(m))
    print(validate_phone(n))
