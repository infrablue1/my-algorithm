"""
Leetcode link: https://leetcode.com/problems/valid-sudoku/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily
solvable. Only the filled cells need to be validated according to the
mentioned rules.

example:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    n = 9
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)
    box_dict = defaultdict(set)

    for i in range(n):
        for j in range(n):
            value = board[i][j]
            if value == '.':
                continue
            if value in row_dict[i] or value in col_dict[j] or \
               value in box_dict[(i // 3, j // 3)]:
                return False
            row_dict[i].add(value)
            col_dict[j].add(value)
            box_dict[(i // 3, j // 3)].add(value)

    return True
