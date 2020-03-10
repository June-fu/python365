#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/9
"""
列表中的元素统计
Counter module
"""


# finding frequency of each element in a list
def most_comm(lst):
    from collections import Counter
    return Counter(lst).most_common(1)


def is_anagram(str1, str2):
    from collections import Counter
    s1, s2 = Counter(str1), Counter(str2)
    return s1 == s2


if __name__ == '__main__':
    from collections import Counter
    m_lst = ['j', 'd', 'j', 'd', 'r', 'd', 'h', 't', 'j', 't', 'j']
    c = Counter(m_lst)
    print(c)
    print(c.most_common(3))

    print(most_comm(m_lst))

    s11, s12 = 'abcde', 'bceda'
    print(is_anagram(s11, s12))
