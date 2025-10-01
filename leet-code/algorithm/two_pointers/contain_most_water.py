"""
Leetcode link: https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i,height[i]).
Find two lines that together with the x-axis form a container, such that the
container contains the most water.
Return the maximum amount of water a container can store.

example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
container can contain is 49.
"""


def maxArea(height: list[int]) -> int:
    n = len(height)
    l, r = 0, n - 1

    ans = 0
    while l < r:
        ans = max(ans, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans
