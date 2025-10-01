"""
Leetcode link: https://leetcode.com/problems/rotate-array/
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rotate_v1(nums: list[int], k: int) -> None:
    def reverse(begin, end):
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1

    n = len(nums)
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


def rotate_v2(nums: list[int], k: int) -> None:
    tmp_nums = nums.copy()
    n = len(nums)

    for i in range(n):
        nums[(i + k) % n] = tmp_nums[i]
