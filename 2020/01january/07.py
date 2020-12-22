# -*- coding: utf-8 -*-

# Author: june-fu
# Date  : 2020/1/20
"""
Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return “True” if the given array A is monotonic else return “False” (without quotes).

Input : [6, 5, 4, 4]
Output : true

Input : [5, 12, 3, 5]
Output : false
"""


def is_monotonic(arr):
    for a in range(len(arr)-1):
        if arr[a] != arr[a+1]:
            j = a
            break

    if arr[j] < arr[j+1]:
        for i in range(j, len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
    elif arr[j] > arr[j+1]:
        for i in range(j, len(arr) - 1):
            if arr[i] < arr[i+1]:
                return False
    return True


def is_monotonic2(arr):
    return (all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or
            all(arr[i] >= arr[i+1] for i in range(len(arr)-1)))


if __name__ == '__main__':
    arr1 = [6, 5, 4, 4]
    arr2 = [5, 12, 3, 5]
    arr3 = [4, 4, 4, 2, 1]
    print(is_monotonic(arr1))
    print(is_monotonic(arr2))
    print(is_monotonic(arr3))

    print("is_monotonic2:", is_monotonic2(arr1))
    print("is_monotonic2:", is_monotonic2(arr2))
    print("is_monotonic2:", is_monotonic2(arr3))
