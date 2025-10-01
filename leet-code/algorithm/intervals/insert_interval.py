"""
Leetcode link: https://leetcode.com/problems/insert-interval/
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the ith
interval and intervals is sorted in ascending order by starti. You are also
given an interval newInterval = [start, end] that represents the start and end
of another interval. Insert newInterval into intervals such that intervals is
still sorted in ascending order by starti and intervals still does not have any
overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array
and return it.

example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""


def insert(intervals: list[list[int]], newInterval: list[int]):
    if len(intervals) == 0:
        return [newInterval]

    index = 0
    for i in range(1, len(intervals)):
        if newInterval[0] <= intervals[i][0]:
            index = i
            break
    tmp = intervals[:index] + [newInterval] + intervals[index:]

    # Merge intervals.
    start, end = tmp[0][0], tmp[0][1]
    ans = []
    for interval in tmp[1:]:
        a, b = interval[0], interval[1]
        if a >= start and a <= end:
            end = max(end, b)
        else:
            ans.append([start, end])
            start, end = a, b
    ans.append([start, end])

    return ans
