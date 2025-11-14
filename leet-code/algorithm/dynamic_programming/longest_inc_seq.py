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

# Binary search solution
def lengthOfLIS2(nums: list[int]) -> int:
    n = len(nums)
    tails =[0] * n
    size = 0
    for num in nums:
        i, j = 0, size
        while i < j:
            mid = (i + j) // 2
            if tails[mid] < num:
                i = mid + 1
            else:
                j = mid
        tails[i] = num
        size = max(i + 1, size)

    return size
