"""
Leetcode link: https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""


def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    maxLeft, maxRight, maxCount = 0, 0, 1
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
                count = i - j + 1
                if count > maxCount:
                    maxLeft, maxRight, maxCount = j, i, count

    return s[maxLeft:maxRight + 1]
