"""
Leetcode link: https://leetcode.com/problems/game-of-life/
According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway
in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial
state: live (represented by a 1) or dead (represented by a 0). Each cell
interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by
under-population.
2. Any live cell with two or three live neighbors lives on to the next
generation.
3. Any live cell with more than three live neighbors dies, as if by
over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if
by reproduction.

The next state of the board is determined by applying the above rules
simultaneously to every cell in the current state of the m x n grid board.
In this process, births and deaths occur simultaneously.
Given the current state of the board, update the board to reflect its next
state.

example:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""


def gameOfLife(board: list[list[int]]) -> None:
    m, n = len(board), len(board[0])
    live_count_matrix = [[0 for _ in range(n)] for _ in range(m)]

    # Collect live count of its neighbors.
    def collec_count(x: int, y: int):
        live_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    live_count += board[nx][ny]

        return live_count

    for i in range(m):
        for j in range(n):
            live_count_matrix[i][j] = collec_count(i, j)

    for i in range(m):
        for j in range(n):
            # Current state is dead, it will become live on if it has 3 live
            # neighbors.
            if board[i][j] == 0:
                if live_count_matrix[i][j] == 3:
                    board[i][j] = 1
            # Current state is live, it will become dead if the amount of live
            # neighbors is less than 2 or greater than 3.
            else:
                if live_count_matrix[i][j] < 2 or live_count_matrix[i][j] > 3:
                    board[i][j] = 0
