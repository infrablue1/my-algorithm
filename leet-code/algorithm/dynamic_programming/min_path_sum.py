"""
Leetcode link: https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

example:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""


def minPathSum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = grid.copy()

    for i in range(1, m):
        dp[i][0] += dp[i - 1][0]
    for j in range(1, n):
        dp[0][j] += dp[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])

    return dp[m - 1][n - 1]
