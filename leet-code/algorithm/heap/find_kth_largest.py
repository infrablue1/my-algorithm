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

    def quickSelect(nums: list[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return quickSelect(left, k)
        elif k > L + M:
            return quickSelect(right, k - L - M)
        return mid[0]

    # K is the kth smallest.
    K = len(nums) - k + 1
    return quickSelect(nums, K)
