"""
Leetcode link: https://leetcode.com/problems/maximal-square/
Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

example:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
                 ["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
"""


def maximalSquare(matrix: list[list[str]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    ans = 0

    for i in range(m):
        dp[i][0] = int(matrix[i][0])
        ans = max(ans, dp[i][0])
    for j in range(n):
        dp[0][j] = int(matrix[0][j])
        ans = max(ans, dp[0][j])

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j - 1],
                               min(dp[i - 1][j], dp[i][j - 1])) + 1
                ans = max(ans, dp[i][j])

    return ans * ans
