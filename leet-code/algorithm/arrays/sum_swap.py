"""
Leetcode link: https://leetcode.cn/problems/sum-swap-lcci/
Given two arrays of integers, find a pair of values (one value from each array)
that you can swap to give the two arrays the same sum. Return an array, where
the first element is the element in the first array that will be swapped, and
the second element is another one in the second array. If there are more than
one answers, return any one of them. If there is no answer, return an empty
array.

example:
Input: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
Output: [1, 3]
"""


def findSwapValues(array1: list[int], array2: list[int]) -> list[int]:
    array1.sort()
    array2.sort()
    sum1, sum2 = sum(array1), sum(array2)
    if (sum1 - sum2) % 2 != 0:
        return []
    diff = int((sum1 - sum2) / 2)

    i, j = 0, 0
    m, n = len(array1), len(array2)
    while i < m and j < n:
        if array1[i] - array2[j] < diff:
            i += 1
        elif array1[i] - array2[j] > diff:
            j += 1
        else:
            return [array1[i], array2[j]]
    return []
