"""
Leetcode link:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted
-array/
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value. If target is not found in
the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


def searchRange(nums: list[int], target: int) -> list[int]:
    def search(firstPos: bool) -> int:
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                if firstPos:
                    right = mid - 1
                else:
                    left = mid + 1

        return index

    return [search(True), search(False)]
