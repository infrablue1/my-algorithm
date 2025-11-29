"""
Leetcode link: https://leetcode.cn/problems/exchange-lcci/
Write a program to swap odd and even bits in an integer with as few
instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3
are swapped, and so on).

example:
Input: num = 2（0b10）
Output 1 (0b01)
"""


def exchangeBits(num: int) -> int:
    odd = num & 0x55555555
    even = num & 0xaaaaaaaa
    return (odd << 1) | (even >> 1)
