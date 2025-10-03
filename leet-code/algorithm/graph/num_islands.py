"""
Leetcode link: https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


def numIslands(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    vis = [[False for _ in range(n)] for _ in range(m)]
    ans = 0

    def dfs(x: int, y: int) -> None:
        vis[x][y] = True
        steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and \
                    not vis[nx][ny] and grid[nx][ny] == '1':
                dfs(nx, ny)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not vis[i][j]:
                ans += 1
                dfs(i, j)

    return ans
