"""
Leetcode link: https://leetcode.cn/problems/convert-integer-lcci/
Write a function to determine the number of bits you would need to flip to
convert integer A to integer B.

example:
Input: A = 29 (0b11101), B = 15 (0b01111)
Output: 2
"""


def convertInteger(A: int, B: int) -> int:
    tmp = A ^ B
    ans = 0
    for _ in range(32):
        ans += tmp & 1
        tmp >>= 1
    return ans
