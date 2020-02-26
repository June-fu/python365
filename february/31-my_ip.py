#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/2/26
"""
Problem 10: Write a program myip.py to print the external IP address of the machine.
 Use the response from http://httpbin.org/get and read the IP address from there.
 The program should print only the IP address and nothing else.
"""


def my_ip(url):
    from urllib import request
    import json
    import re

    json_data = json.loads(request.urlopen(url).read())
    print(json_data)
    for v in json_data.values():
        if re.fullmatch(r'[\d.]{4,}', str(v)):
            print(re.findall(r'[\d.]{4,}', str(v)))


if __name__ == '__main__':
    my_ip('http://httpbin.org/get')
