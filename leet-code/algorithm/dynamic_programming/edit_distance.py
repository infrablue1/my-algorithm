"""
Leetcode link: https://leetcode.com/problems/edit-distance/
Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.
You have the following three operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

example:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:
"""


def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            x, y = i - 1, j - 1
            if word1[x] == word2[y]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1],
                               min(dp[i - 1][j], dp[i][j - 1])) + 1

    return dp[m][n]
