"""
Leetcode link: https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.
"""


def trap(height: list[int]) -> int:
    n = len(height)
    left = [0] * n
    right = [0] * n
    left[0] = height[0]
    right[n - 1] = height[n - 1]

    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    ans = 0
    for i in range(1, n - 1):
        h = min(left[i - 1], right[i + 1])
        ans += max(0, h - height[i])

    return ans
