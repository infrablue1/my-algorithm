"""
Leetcode link: https://leetcode.cn/problems/magic-index-lcci/
A magic index in an array A[0...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of integers, write a method to find a magic
index, if one exists, in array A. If not, return -1. If there are more than one
magic index, return the smallest one.

example:
Input: nums = [0, 2, 3, 4, 5]
Output: 0
"""


def findMagicIndex(nums: list[int]) -> int:
    n = len(nums)

    def dfs(left: int, right: int):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        leftResult = dfs(left, mid - 1)
        if leftResult != -1:
            return leftResult
        if nums[mid] == mid:
            return mid
        return dfs(mid + 1, right)

    return dfs(0, n - 1)
