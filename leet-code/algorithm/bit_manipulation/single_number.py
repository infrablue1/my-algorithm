"""
Leetcode link: https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one. You must implement a solution with a linear
runtime complexity and use only constant extra space.

example:
Input: nums = [2,2,1]
Output: 1
"""


def singleNumber(nums: list[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans


"""
Leetcode link: https://leetcode.com/problems/single-number-ii/
Given an integer array nums where every element appears three times except for
one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only
constant extra space.

example:
Input: nums = [2,2,3,2]
Output: 3
"""


def singleNumber2(nums: list[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones
