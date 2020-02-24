#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/25
"""
Problem 5: Write a program wget.py to download a given URL.
The program should accept a URL as argument, download it and save it with the basename of the URL.
If the URL ends with a /, consider the basename as index.html.

$ python wget.py http://docs.python.org/tutorial/interpreter.html
saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.

$ python wget.py http://docs.python.org/tutorial/
saving http://docs.python.org/tutorial/ as index.html.
"""


def wget(url):
    from urllib import request

    if url[-1] == '/':
        print(f'saving {url} as index.html')
        request.urlretrieve(url, 'index.html')
    else:
        print(f'saving {url} as {url.split("/")[-1]}')
        request.urlretrieve(url, url.split('/')[-1])


if __name__ == '__main__':
    wget("http://docs.python.org/tutorial/")
    wget('http://docs.python.org/tutorial/interpreter.html')
