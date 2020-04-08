#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/4/8
"""
CtCI-6th-Edition
page78:判定字符是否唯一：确定一个字符串的所有字符是否全都不同；假设不循序使用额外的数据结构，又该怎么处理？
"""
import unittest


def unique(string):
    return len(string) == len(set(string))


def is_unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for s in string:
        if char_set[ord(s)]:
            return False
        char_set[ord(s)] = True
    return True


class Test(unittest.TestCase):
    dataT = ['abcd', 's4fad', '']
    dataF = ['23ds2', 'hb 627jh=j ()']

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
