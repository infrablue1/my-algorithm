"""
Leetcode link: https://leetcode.com/problems/set-matrix-zeroes/
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's. You must do it in place.

example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])

    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # Move zero to the first row and the first column.
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j], matrix[i][0] = 0, 0

    # Check whether border row or column has value of 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # At last set border.
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
