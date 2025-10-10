"""
Leetcode link: https://leetcode.com/problems/longest-increasing-subsequence/
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
"""


def lengthOfLIS(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    ans = 1

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
    return ans
