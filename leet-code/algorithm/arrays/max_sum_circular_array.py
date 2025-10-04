"""
Leetcode link: https://leetcode.com/problems/maximum-sum-circular-subarray/
Given a circular integer array nums of length n, return the maximum possible
sum of a non-empty subarray of nums. A circular array means the end of the
array connects to the beginning of the array. Formally, the next element of
nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is
nums[(i - 1 + n) % n]. A subarray may only include each element of the fixed
buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ...,
nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

example:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
"""


def maxSubarraySumCircular(nums: list[int]) -> int:
    curMax, curMin = 0, 0
    maxSum, minSum = nums[0], nums[0]
    total = 0

    for num in nums:
        curMax = max(num, curMax + num)
        maxSum = max(curMax, maxSum)
        curMin = min(num, curMin + num)
        minSum = min(curMin, minSum)
        total += num

    if maxSum > 0:
        return max(maxSum, total - minSum)
    return maxSum
