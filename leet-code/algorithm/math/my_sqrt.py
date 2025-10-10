"""
Leetcode link: https://leetcode.com/problems/sqrtx/
Given a non-negative integer x, return the square root of x rounded down to the
nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

example:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
"""


def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid == x // mid:
            return mid
        if mid < x // mid:
            left = mid + 1
        else:
            right = mid - 1

    return right
