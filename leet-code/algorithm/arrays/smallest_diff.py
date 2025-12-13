"""
Leetcode link: https://leetcode.cn/problems/smallest-difference-lcci/
Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference.

example:
Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
Output:  3, the pair (11, 8)
"""


def smallestDifference(a: list[int], b: list[int]) -> int:
    a.sort()
    b.sort()
    ans = 2 ** 31 - 1
    i, j = 0, 0
    m, n = len(a), len(b)

    while i < m and j < n:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    return ans
