"""
Leetcode link: https://leetcode.cn/problems/best-line-lcci/
Given a two-dimensional graph with points on it, find a line which passes the
most number of points. Assume all the points that passed by the line are
stored in list S sorted by their number. You need to return [S[0], S[1]], that
is , two points that have smallest number. If there are more than one line that
passes the most number of points, choose the one that has the smallest S[0].
If there are more that one line that has the same S[0], choose the one that has
smallest S[1].

example:
Input:  [[0,0],[1,1],[1,0],[2,0]]
Output:  [0,2]
Explanation:  The numbers of points passed by the line are [0,2,3].
"""

from collections import defaultdict


def bestLine(points: list[list[int]]) -> list[int]:
    maxPoint = 0
    ans = []
    n = len(points)

    for i in range(n):
        x1, y1 = points[i][0], points[i][1]
        slopeDict = defaultdict(list)
        for j in range(i + 1, n):
            x2, y2 = points[j][0], points[j][1]
            if x1 == x2:
                slopeDict["inf"].append(j)
            else:
                k = (y2 - y1) / (x2 - x1)
                slopeDict[k].append(j)

        for k in slopeDict:
            if len(slopeDict[k]) + 1 > maxPoint:
                maxPoint = len(slopeDict[k]) + 1
                ans = [i] + slopeDict[k]

    return ans[:2]
