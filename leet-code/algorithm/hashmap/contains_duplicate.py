"""
Leetcode link: https://leetcode.com/problems/contains-duplicate-ii/
Given an integer array nums and an integer k, return true if there are two
distinct indices i and j in the array such that
nums[i] == nums[j] and abs(i - j) <= k.

example:
Input: nums = [1,2,3,1], k = 3
Output: true
"""


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    num2index = {}
    for i in range(len(nums)):
        if nums[i] in num2index:
            if abs(i - num2index[nums[i]]) <= k:
                return True

        num2index[nums[i]] = i

    return False
