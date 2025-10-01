"""
Leetcode link: https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

example:
Input: nums = [3,2,3]
Output: 3
"""


def majorityElement(nums: list[int]) -> int:
    value = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            value = nums[i]

        count += 1 if nums[i] == value else -1

    return value
