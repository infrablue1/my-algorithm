
"""
Leetcode link: https://leetcode.com/problems/merge-sorted-array/description

You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.
"""


def mergeSortedArray(nums1: list[int], m: int, nums2: list[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = m - 1, n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
