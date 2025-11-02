"""
Leetcode link: https://leetcode.cn/problems/robot-in-a-grid-lcci/
Imagine a robot sitting on the upper left corner of grid with r rows and c
columns. The robot can only move in two directions, right and down, but certain
cells are "off limits" such that the robot cannot step on them. Design an
algorithm to find a path for the robot from the top left to the bottom right.

example:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: [[0,0],[0,1],[0,2],[1,2],[2,2]]
"""


def pathWithObstacles(obstacleGrid: list[list[int]]) -> list[list[int]]:
    if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
        return []
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    ans = []
    vis = [[False for _ in range(n)] for _ in range(m)]

    def dfs(x: int, y: int) -> bool:
        if x >= m or y >= n or obstacleGrid[x][y] == 1 or vis[x][y]:
            return False
        ans.append([x, y])
        vis[x][y] = True
        if x == m - 1 and y == n - 1:
            return True
        if dfs(x + 1, y) or dfs(x, y + 1):
            return True
        ans.pop()
        return False

    dfs(0, 0)
    return ans
