"""
Leetcode link: https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

example:
Input: s = "anagram", t = "nagaram"
Output: true
"""


def isAnagram(s: str, t: str) -> bool:
    count_list = [0] * 26
    for ch in s:
        count_list[ord(ch) - ord('a')] += 1
    for ch in t:
        count_list[ord(ch) - ord('a')] -= 1

    return all(count == 0 for count in count_list)
