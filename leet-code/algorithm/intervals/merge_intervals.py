"""
Leetcode link: https://leetcode.com/problems/merge-intervals/
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0][0], intervals[0][1]
    ans = []

    for interval in intervals[1:]:
        a, b = interval[0], interval[1]
        if a >= start and a <= end:
            end = max(end, b)
        else:
            ans.append([start, end])
            start, end = a, b
    ans.append([start, end])

    return ans
