"""
Leetcode link: https://leetcode.com/problems/reverse-bits/
Reverse bits of a given 32 bits signed integer.

example:
Input: n = 43261596
Output: 964176192
"""


def reverseBits(n: int) -> int:
    ans = 0
    for _ in range(32):
        bit = n & 1
        ans = (ans << 1) | bit
        n >>= 1
    return ans
