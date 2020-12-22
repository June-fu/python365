# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/19
"""
Reversal algorithm for array rotation
just like 05: Write a function rotate(ar[], d) that rotates arr[] by d elements.
but you should use reversal algorithm

rotate(arr[], d)
  reverse(arr[], 1, d) ;
  reverse(arr[], d + 1, n);
  reverse(arr[], 1, n);
"""


# Function to reverse arr[] from index start to end
def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def left_rotate(arr, d):
    if d == 0:
        return
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, len(arr)-1)
    reverse_array(arr, 0, len(arr)-1)
    return arr


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    print(left_rotate(arr1, 2))




