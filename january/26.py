#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/1/31
"""
Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word.
Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
input: python wordwrap.py she.txt 30
I'm sure that the shells are
seashore shells.
So if she sells seashells on
the seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the
seashore;
"""


def wordwrap(filename, width):
    lst = []
    with open(filename) as f:
        for line in f.readlines():
            if len(line) > width:
                x = line[:width].rfind(' ')
                lst.append(line[:x] + '\n' + line[x:].lstrip())
            else:
                lst.append(line)
    return ''.join(lst)


if __name__ == '__main__':
    import sys
    file_name, w = sys.argv[1], sys.argv[2]

    print(wordwrap(file_name, int(w)))
