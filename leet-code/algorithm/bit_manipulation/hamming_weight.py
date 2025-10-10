"""
Leetcode link: https://leetcode.com/problems/number-of-1-bits/
Given a positive integer n, write a function that returns the number of set
bits in its binary representation (also known as the Hamming weight).

example:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.
"""


def hammingWeight(n: int) -> int:
    ans = 0
    while n > 0:
        ans += n & 1
        n >>= 1
    return ans
