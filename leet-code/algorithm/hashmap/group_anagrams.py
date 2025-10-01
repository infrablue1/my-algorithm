"""
Leetcode link: https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
1. There is no string in strs that can be rearranged to form "bat".
2. The strings "nat" and "tan" are anagrams as they can be rearranged to form
each other.
3. The strings "ate", "eat", and "tea" are anagrams as they can be rearranged
to form each other.
"""

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans[tuple(count)].append(s)

    values = list(ans.values())
    for value in values:
        value.sort()
    values.sort(key=lambda value: len(value))

    return values
