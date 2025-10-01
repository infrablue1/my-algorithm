"""
Leetcode link: https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of words and spaces, return the length of the last
word in the string.
A word is a maximal substring consisting of non-space characters only.

example:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""


def lengthOfLastWord(s: str) -> int:
    right = len(s) - 1
    while right >= 0 and s[right] == ' ':
        right -= 1

    left = right
    while left >= 0 and s[left] != ' ':
        left -= 1

    return right - left
