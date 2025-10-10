"""
Leetcode link: https://leetcode.com/problems/triangle/
Given a triangle array, return the minimum path sum from top to bottom. For
each step, you may move to an adjacent number of the row below. More formally,
if you are on index i on the current row, you may move to either index i or
index i + 1 on the next row.

example:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11
(underlined above).
"""


def minimumTotal(triangle: list[list[int]]) -> int:
    height = len(triangle)
    dp = triangle[-1].copy()

    for i in range(height - 2, -1, -1):
        layer = triangle[i]
        width = len(layer)
        for j in range(width):
            dp[j] = min(dp[j], dp[j + 1]) + layer[j]

    return dp[0]
