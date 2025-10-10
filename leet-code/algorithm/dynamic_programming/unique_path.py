"""
Leetcode link: https://leetcode.com/problems/unique-paths-ii/
You are given an m x n integer array grid. There is a robot initially located
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time. An obstacle and space are marked as 1 or 0
respectively in grid. A path that the robot takes cannot include any square
that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

example:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

    for i in range(1, m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = dp[0][0]
    for j in range(1, n):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = dp[0][0]

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            x = dp[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0
            y = dp[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0
            dp[i][j] = x + y

    return dp[m - 1][n - 1]
