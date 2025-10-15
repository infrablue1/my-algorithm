"""
Leetcode link: https://leetcode.cn/problems/max-submatrix-lcci/
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条
件的子矩阵，返回任意一个均可。

example:
输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
"""


def getMaxMatrix(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len((matrix[0]))
    preSum = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                preSum[i][j] = matrix[i][j]
            else:
                preSum[i][j] = matrix[i][j] + preSum[i - 1][j]

    r1, r2 = 0, 0
    maxValue = preSum[0][0]
    ans = [0, 0, 0, 0]
    for startRow in range(m):
        for endRow in range(startRow, m):
            total = 0
            c1, c2 = 0, 0
            for col in range(n):
                val = preSum[endRow][col] - preSum[startRow - 1][col] \
                    if startRow > 0 else preSum[endRow][col]
                if total < 0:
                    c1 = col
                    total = 0
                total += val
                if total > maxValue:
                    maxValue = total
                    r1, r2 = startRow, endRow
                    c2 = col
                    ans = [r1, c1, r2, c2]
    return ans
