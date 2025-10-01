"""
Leetcode link: https://leetcode.com/problems/spiral-matrix/
Given an m x n matrix, return all elements of the matrix in spiral order.

example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    row, col = 0, 0
    count = 0
    ans = []
    step_idx = 0
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while count < m * n:
        ans.append(matrix[row][col])
        matrix[row][col] = '.'
        count += 1

        x, y = steps[step_idx]
        ncol, nrow = row + x, col + y
        if ncol >= m or nrow >= n or matrix[ncol][nrow] == '.':
            step_idx = (step_idx + 1) % len(steps)
            x, y = steps[step_idx]
            ncol, nrow = row + x, col + y

        row, col = ncol, nrow

    return ans
