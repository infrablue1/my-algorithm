"""
Leetcode link: https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of
strings. If there is no common prefix, return an empty string ""..

example:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longestCommonPrefix(strs: list[str]) -> str:
    shortest = min(strs, key=len)

    for i, ch in enumerate(shortest):
        for s in strs:
            if s[i] != ch:
                return shortest[:i]

    return shortest
