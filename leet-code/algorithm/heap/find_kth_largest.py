"""
Leetcode link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Given an integer array nums and an integer k, return the kth largest element in
the array. Note that it is the kth largest element in the sorted order, not the
kth distinct element.
Can you solve it without sorting?

example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""

import random


def findKthLargest(nums: list[int], k: int) -> int:

    def partition(left, right) -> int:
        randomIndex = random.randint(left, right)
        nums[randomIndex], nums[left] = nums[left], nums[randomIndex]
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    def quickSelect(left: int, right: int, k: int) -> int:
        if left >= right:
            return
        pos = partition(left, right)
        index = pos - left + 1
        if k == index:
            return
        elif k < index:
            quickSelect(left, pos - 1, k)
        else:
            quickSelect(pos + 1, right, k - index)

    K = len(nums) - k + 1
    quickSelect(0, len(nums) - 1, K)
    return nums[K - 1]
