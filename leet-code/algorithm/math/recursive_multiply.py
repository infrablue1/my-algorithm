"""
Leetcode link: https://leetcode.cn/problems/recursive-mulitply-lcci/
Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you
should minimize the number of those operations.

example:
Input: A = 1, B = 10
Output: 10
"""


def multiply(A: int, B: int) -> int:
    ans = 0
    while B > 0:
        if B & 1:
            ans += A
        A <<= 1
        B >>= 1
    return ans
