"""
Leetcode link: https://leetcode.cn/problems/peaks-and-valleys-lcci/
In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and a "valley" is an element which is less than or
equal to the adjacent inte­gers. For example, in the array {5, 8, 4, 2, 3, 4,
6}, {8, 6} are peaks and {5, 2} are valleys. Given an array of integers, sort
the array into an alternating sequence of peaks and valleys.

example:
Input: [5, 3, 1, 2, 3]
Output: [5, 1, 3, 2, 3]
"""


def wiggleSort(nums: list[int]) -> list[int]:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(1, n):
        if i % 2 == 0:
            # peak value must be greater than its left.
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        else:
            # valley value must be less than its left.
            if nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums.copy()
