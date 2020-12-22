# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/29
"""
Problem 13: Write a function lensort to sort a list of strings based on length.
input: lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
output: ['c', 'perl', 'java', 'ruby', 'python', 'haskell']

Problem 14:Improve the unique function written in previous problems to take an optional key function as argument
and use the return value of the key function to check for uniqueness.
input: unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
output: ["python", "java"]
"""


def len_sort(list_str):
    list_str.sort(key=lambda x: len(x))
    return list_str


def unique(list1, key):
    seen = set()
    return [key(x) for x in list1 if key(x) not in seen and not seen.add(x)]


if __name__ == '__main__':
    sorted_list = len_sort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
    print(sorted_list)

    y = unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
    print(y)
