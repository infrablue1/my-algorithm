"""
Leetcode link: https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return
its sum.

example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""


def maxSubArray(nums: list[int]) -> int:
    ans = nums[0]
    total = 0
    for num in nums:
        total = max(total, 0)
        total += num
        ans = max(ans, total)

    return ans
