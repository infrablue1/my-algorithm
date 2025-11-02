"""
Leetcode link: https://leetcode.cn/problems/one-away-lcci/
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write
a function to check if they are one edit (or zero edits) away.

example:
Input:
first = "pale"
second = "ple"
Output: True
"""


def oneEditAway(first: str, second: str) -> bool:
    n1, n2 = len(first), len(second)
    if n1 == n2:
        diffCount = 0
        for i in range(n1):
            if first[i] != second[i]:
                diffCount += 1
            if diffCount > 1:
                return False
        return True
    elif abs(n1 - n2) == 1:
        if n1 > n2:
            n1, n2 = n2, n1
            first, second = second, first

        i, j = 0, 0
        while i < n1 and j < n2:
            if first[i] == second[j]:
                i += 1
            j += 1
            if j - i > 1:
                return False
        return True
    return False
