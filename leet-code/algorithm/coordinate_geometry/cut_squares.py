"""
Leetcode link: https://leetcode.cn/problems/bisect-squares-lcci/
Given two squares on a two-dimensional plane, find a line that would cut these
two squares in half. Assume that the top and the bottom sides of the square run
parallel to the x-axis. Each square consists of three values, the coordinate of
bottom left corner [X,Y] = [square[0],square[1]], and the side length of the
square square[2]. The line will intersect to the two squares in four points.
Return the coordinates of two intersection points [X1,Y1] and [X2,Y2] that the
forming segment covers the other two intersection points in format of
{X1,Y1,X2,Y2}. If X1 != X2, there should be X1 < X2, otherwise there should
be Y1 <= Y2.
If there are more than one line that can cut these two squares in half, return
the one that has biggest slope (slope of a line parallel to the y-axis is
considered as infinity).

example:
Input:
square1 = {-1, -1, 2}
square2 = {0, -1, 2}
Output: {-1,0,2,0}
Explanation: y = 0 is the line that can cut these two squares in half.
"""


def cutSquares(square1: list[int], square2: list[int]) -> list[float]:
    # Caluculate the center of each square.
    len1, len2 = square1[2], square2[2]
    x1, y1 = square1[0] + len1 / 2, square1[1] + len1 / 2
    x2, y2 = square2[0] + len2 / 2, square2[1] + len2 / 2

    ans = [0.0] * 4
    # y = kx +b
    # k is +inf.
    if x1 == x2:
        ans[0] = x1
        ans[1] = min(square1[1], square2[1])
        ans[2] = x1
        ans[3] = max(square1[1] + len1, square2[1] + len2)
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y1 - k * x1
        # The intersection of x is fixed.
        # y = kx + b
        if abs(k) < 1:
            ans[0] = min(square1[0], square2[0])
            ans[1] = k * ans[0] + b
            ans[2] = max(square1[0] + len1, square2[0] + len2)
            ans[3] = k * ans[2] + b
        # The intersection of y is fixed.
        # x = (y - b) / k
        else:
            ans[1] = min(square1[1], square2[1])
            ans[0] = (ans[1] - b) / k
            ans[3] = max(square1[1] + len1, square2[1] + len2)
            ans[2] = (ans[3] - b) / k

    if ans[0] > ans[2]:
        # swap point
        ans[0], ans[2] = ans[2], ans[0]
        ans[1], ans[3] = ans[3], ans[1]

    return ans
