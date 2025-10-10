"""
Leetcode link: https://leetcode.com/problems/bitwise-and-of-numbers-range/
Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.

example:
Input: left = 5, right = 7
Output: 4
"""


def rangeBitwiseAnd(left: int, right: int) -> int:
    count = 0
    while left != right:
        left >>= 1
        right >>= 1
        count += 1

    return left << count
