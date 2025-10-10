"""
Leetcode link: https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the
segmentation.

example:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""


def wordBreak(s: str, wordDict: list[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    wordSet = set(wordDict)

    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]
