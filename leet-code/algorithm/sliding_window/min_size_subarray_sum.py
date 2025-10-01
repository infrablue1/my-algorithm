"""
Leetcode link: https://leetcode.com/problems/minimum-size-subarray-sum/
Given an array of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem
constraint.
"""


def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    left = 0
    ans = n + 1
    cur_sum = 0

    for right in range(n):
        cur_sum += nums[right]

        while cur_sum >= target:
            ans = min(ans, right - left + 1)
            cur_sum -= nums[left]
            left += 1

    return 0 if ans == n + 1 else ans
