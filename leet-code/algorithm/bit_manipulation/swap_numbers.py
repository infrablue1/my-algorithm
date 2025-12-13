"""
Leetcode link: https://leetcode.cn/problems/swap-numbers-lcci/
Write a function to swap a number in place (that is, without temporary
variables).

example:
Input: numbers = [1,2]
Output: [2,1]
"""


def swapNumbers(numbers: list[int]) -> list[int]:
    # (a^b)^a = (a^a)^b = 0^b = b
    numbers[0] ^= numbers[1]
    numbers[1] ^= numbers[0]
    numbers[0] ^= numbers[1]
    return numbers
