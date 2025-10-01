"""
Leetcode link:
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without duplicate
characters.

example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    n = len(s)
    left = 0
    ans = 0

    for right in range(0, n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        ans = max(ans, right - left + 1)

    return ans
