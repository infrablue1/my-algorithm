"""
Leetcode link: https://leetcode.cn/problems/sub-sort-lcci/
Given an array of integers, write a method to find indices m and n such that if
you sorted elements m through n, the entire array would be sorted. Minimize
n - m (that is, find the smallest such sequence).
Return [m,n]. If there are no such m and n (e.g. the array is already sorted),
return [-1, -1].

example:
Input:  [1,2,4,7,10,11,7,12,6,7,16,18,19]
Output:  [3,9]
"""


def subSort(array: list[int]) -> list[int]:
    first, last = -1, -1
    if len(array) == 0:
        return [first, last]
    curMax, curMin = min(array), max(array)
    n = len(array)

    for i in range(n):
        if array[i] < curMax:
            last = i
        else:
            curMax = array[i]
    for i in range(n-1, -1, -1):
        if array[i] > curMin:
            first = i
        else:
            curMin = array[i]

    return [first, last]
