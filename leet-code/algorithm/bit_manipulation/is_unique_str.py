"""
Leetcode link: https://leetcode.cn/problems/is-unique-lcci/
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?

example:
Input: s = "leetcode"
Output: false
"""


def isUnique(astr: str) -> bool:
    flag = 0
    for c in astr:
        shiftBit = ord(c) - ord('a')
        value = 1 << shiftBit
        if flag & value:
            return False
        flag |= value
    return True
