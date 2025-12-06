"""
Leetcode link: https://leetcode.cn/problems/reverse-bits-lcci/
You have an integer and you can flip exactly one bit from a 0 to a 1. Write
code to find the length of the longest sequence of 1s you could create.

example:
Input: num = 1775(110111011112)
Output: 8
"""


def flipOneBit(num: int) -> int:
    length = 0
    newLength = 0
    ans = 1
    for i in range(32):
        if num & (1 << i):
            length += 1
            newLength += 1
        else:
            newLength = length + 1
            length = 0
        ans = max(ans, newLength)
    return ans

