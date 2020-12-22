#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/16
"""
Problem 36: Write a program to find anagrams in a given list of words.
Two words are called anagrams if one word can be formed by rearranging letters of another.
For example 'eat', 'ate' and 'tea' are anagrams.

>>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
[['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
"""


def anagrams(lst):
    d = {}
    for word in lst:
        c = ''.join(sorted([x for x in word]))
        if c not in d.keys():
            d[c] = [word]
        else:
            d[c].append(word)
    return [x for x in d.values()]


if __name__ == '__main__':
    print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
