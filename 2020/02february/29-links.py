#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/25
"""
Problem 8: Write a program links.py that takes URL of a webpage as argument
and prints all the URLs linked from that webpage.
"""


def links(url):
    from urllib import request
    import re

    web_page = request.urlopen(url).read()

    for u in re.findall(r'http[s]*://[\w.]+[/\w.]+', str(web_page)):
        print(u)


if __name__ == '__main__':
    links('http://docs.python.org/tutorial/interpreter.html')
