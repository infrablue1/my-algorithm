"""
Leetcode link: https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic. Two strings s and
t are isomorphic if the characters in s can be replaced to get t. All
occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.

example:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'
"""


def isIsomorphic(s: str, t: str) -> bool:
    s_ch2index = {}
    t_ch2index = {}

    for i in range(len(s)):
        if s[i] not in s_ch2index:
            s_ch2index[s[i]] = i
        if t[i] not in t_ch2index:
            t_ch2index[t[i]] = i

        if s_ch2index[s[i]] != t_ch2index[t[i]]:
            return False

    return True
