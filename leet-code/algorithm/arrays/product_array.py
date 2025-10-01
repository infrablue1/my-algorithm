"""
Leetcode link: https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i]. The product
of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the
division operation.

example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = nums[i - 1] * prefix[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = nums[i + 1] * suffix[i + 1]

    return [prefix[i] * suffix[i] for i in range(0, n)]
