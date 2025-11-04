"""
Leetcode link: https://leetcode.com/problems/search-a-2d-matrix/
You are given an m x n integer matrix matrix with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the
previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        x, y = mid // n, mid % n
        if matrix[x][y] == target:
            return True
        if matrix[x][y] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


"""
Leetcode link: https://leetcode.cn/problems/sorted-matrix-search-lcci/
Given an M x N matrix in which each row and each column is sorted in ascending
order, write a method to find an element.

Example:
Given matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""


def searchMatrix2(matrix: list[list[int]], target: int) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    m, n = len(matrix), len(matrix[0])
    x, y = 0, n - 1

    while x < m and y >= 0:
        if matrix[x][y] == target:
            return True
        if matrix[x][y] < target:
            x += 1
        else:
            y -= 1
    return False
