"""
Leetcode link: https://leetcode.com/problems/surrounded-regions/
You are given an m x n matrix board containing letters 'X' and 'O', capture
regions that are surrounded:
1. Connect: A cell is connected to adjacent cells horizontally or vertically.
2. Region: To form a region connect every 'O' cell.
3. Surround: The region is surrounded with 'X' cells if you can connect the
region with 'X' cells and none of the region cells are on the edge of the
board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the
original board. You do not need to return anything.

example:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],
["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],
["X","O","X","X"]]
"""


def surroundedRegions(grid: list[list[str]]) -> None:
    m, n = len(grid), len(grid[0])
    vis = [[False for _ in range(n)] for _ in range(m)]

    def dfs(x: int, y: int) -> None:
        vis[x][y] = True
        steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and \
                    not vis[nx][ny] and grid[nx][ny] == 'O':
                dfs(nx, ny)

    # Extend 'O' on boarders.
    for i in range(m):
        if not vis[i][0] and grid[i][0] == 'O':
            dfs(i, 0)
        if not vis[i][n - 1] and grid[i][n - 1] == 'O':
            dfs(i, n - 1)

    for j in range(n):
        if not vis[0][j] and grid[0][j] == 'O':
            dfs(0, j)
        if not vis[m - 1][j] and grid[m - 1][j] == 'O':
            dfs(m - 1, j)

    # Replace non-visited 'O' with 'X'.
    for i in range(m - 1):
        for j in range(n - 1):
            if not vis[i][j] and grid[i][j] == 'O':
                grid[i][j] = 'X'
