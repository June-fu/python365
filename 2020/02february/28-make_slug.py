#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/25
"""
Problem 7: Write a function make_slug that takes a name converts it into a slug.
 A slug is a string where spaces and special characters are replaced by a hyphen,
 typically used to create blog post URL from post title.
 It should also make sure there are no more than one hyphen in any place and
 there are no hyphens at the biginning and end of the slug.

 >>> make_slug("hello world")
'hello-world'
>>> make_slug("hello  world!")
'hello-world'
>>> make_slug(" --hello-  world--")
'hello-world'
"""


def make_slug(str1):
    import re
    str1 = re.sub(r'\s+', '-', str1)
    str1 = re.sub(r'^\W+|\W+$', '', str1)
    str1 = re.sub(r'[-]{2,}', '-', str1)

    print(str1)


def make_slug2(string):
    import re
    lst = re.findall(r'(\w+)', string)
    print('-'.join(lst))


if __name__ == '__main__':
    make_slug("hello world")
    make_slug("hello  world!")
    make_slug2(" --hello-  world--")

