#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: june-fu
# Date  : 2020/3/12
"""
How to make a flat list
当你不确定列表的嵌套深度，但希望将所有元素放在一个平面列表中，该怎么做。
"""
global final_lst


def flat(lst):
    lst = sum(lst, [])  # 效率不高，但很好玩
    final_lst.extend([i for i in lst if type(i) != list])
    # for i in lst:
    #     if type(i) != list:
    #         final_lst.append(i)
    lst = [i for i in lst if i not in final_lst]
    if lst:
        flat(lst)
    return final_lst


def flat1(lst):
    from itertools import chain
    return list(chain.from_iterable(lst))


# this is the final solution
def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    from collections.abc import Iterable

    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


if __name__ == '__main__':
    L = [[1, 2, 3], [4, [5], [6, 7]], [8, [9, [10]]]]
    final_lst = []
    print(flat(L))

    print([i for i in flatten(L)])
