"""
Leetcode link:
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
There are some spherical balloons taped onto a flat wall that represents the
XY-plane. The balloons are represented as a 2D integer array points where
points[i] = [xstart, xend] denotes a balloon whose horizontal diameter
stretches between xstart and xend. You do not know the exact y-coordinates of
the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from
different points along the x-axis. A balloon with xstart and xend is burst by
an arrow shot at x if xstart <= x <= xend. There is no limit to the number of
arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting
any balloons in its path. Given the array points, return the minimum number of
arrows that must be shot to burst all balloons.

example:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
"""


def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[0])
    start, end = points[0][0], points[0][1]
    count = 1

    for point in points[1:]:
        a, b = point[0], point[1]
        if a >= start and a <= end:
            # Update start, end to intersection.
            end = min(b, end)
            start = max(a, start)
        else:
            count += 1
            start, end = a, b

    return count
