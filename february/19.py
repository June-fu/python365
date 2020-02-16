#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/16
"""
Problem 34: Word Frequency
find the number of occurrences of each word in a file.
Then print the words in the descending order of the number of occurrences.
"""


def word_frequency():
    frequency = {}
    with open('a.csv') as f:
        for line in f.readlines():
            line = line.strip()
            for w in line.split(','):
                frequency[w] = frequency.get(w, 0) + 1

    for key, value in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(key, value)


if __name__ == '__main__':
    word_frequency()
