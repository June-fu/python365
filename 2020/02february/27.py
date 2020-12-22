#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/25
"""
Problem 6: Write a program antihtml.py that takes a URL as argument,
 downloads the html from web and print it after stripping html tags.

$ python antihtml.py index.html
...
The Python interpreter is usually installed as /usr/local/bin/python on
those machines where it is available; putting /usr/local/bin in your
...
"""


def anti_html(url):
    from urllib import request
    import re

    f_name = url.split('/')[-1]
    request.urlretrieve(url, f_name)

    with open(f_name, encoding='utf-8') as f:
        content = re.findall(r'>[^>]+<', f.read())  # r'<[^>]+>' 是html标签
        for i in content:
            if i[1:-1].strip():
                print(i[1:-1].strip())


def anti_html2(url):
    from urllib import request
    import re

    f_name = url.split('/')[-1]
    request.urlretrieve(url, f_name)

    with open(f_name, encoding='utf-8') as f:
        content = re.sub(r'<[^>]+>', '', f.read())  # r'<[^>]+>' 是html标签
        for line in re.sub(r"\s{2,}", '~', content).split('~'):
            print(line)


if __name__ == '__main__':
    # anti_html('http://docs.python.org/tutorial/interpreter.html')
    anti_html2('http://docs.python.org/tutorial/interpreter.html')