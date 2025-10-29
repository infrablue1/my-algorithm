"""
Leetcode link: https://leetcode.cn/problems/eight-queens-lcci/
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线
不只是平分整个棋盘的那两条对角线。

example:
 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释：4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


def solveNQueens(n: int) -> list[list[str]]:
    ans = []

    def isSafe(board: list[list[str]], row: int, column: int) -> True:
        return (
            all(board[i][j] != 'Q' for i, j in zip(range(row),
                                                   [column] * row)) and
            all(board[i][j] != 'Q'
                for i, j in zip(range(row - 1, -1, -1),
                                range(column - 1, -1, -1))) and
            all(board[i][j] != 'Q' for i, j in zip(range(row - 1, -1, -1),
                                                   range(column + 1, n)))
        )

    def backtrack(row: int, board: list[list[str]]):
        if row == n:
            ans.append([''.join(x) for x in board])
        else:
            for column in range(n):
                if isSafe(board, row, column):
                    board[row][column] = 'Q'
                    backtrack(row + 1, board)
                    board[row][column] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, board)
    return ans
