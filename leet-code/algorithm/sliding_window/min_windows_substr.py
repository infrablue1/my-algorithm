"""
Leetcode link: https://leetcode.com/problems/minimum-window-substring/
Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".

example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
from string t.
"""


def minWindow(s: str, t: str) -> str:
    map = [0] * 128
    for c in t:
        map[ord(c)] += 1
    n = len(s)
    count = len(t)
    start, end = 0, 0
    minStart, minLength = 0, n + 1

    while end < n:
        c = s[end]
        if map[ord(c)] > 0:
            count -= 1
        map[ord(c)] -= 1
        end += 1

        while count == 0:
            if end - start < minLength:
                minStart = start
                minLength = end - start
            if map[ord(s[start])] == 0:
                count += 1
            map[ord(s[start])] += 1
            start += 1

    return '' if minLength == n + 1 else s[minStart:minStart + minLength]
