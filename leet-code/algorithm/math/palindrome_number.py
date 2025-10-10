"""
Leetcode link: https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is a palindrome, and false otherwise.

example:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    num = x
    tmp = 0
    while num > 0:
        tmp = tmp * 10 + num % 10
        num //= 10
    return tmp == x
