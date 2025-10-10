"""
Leetcode link: https://leetcode.com/problems/factorial-trailing-zeroes/
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

example:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
"""


def trailingZeroes(n: int) -> int:
    ans = 0
    while n > 0:
        n //= 5
        ans += n

    return ans
