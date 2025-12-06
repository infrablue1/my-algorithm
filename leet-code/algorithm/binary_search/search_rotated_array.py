"""
Leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/
There is an integer array nums sorted in ascending order(with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an
unknown index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices
and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation
and an integer target, return the index of target if it is in nums, or -1 if it
is not in nums.
You must write an algorithm with O(log n) runtime complexity.

example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


def searchRotatedArray(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[0] <= nums[mid]:
            # [0, mid] is sorted.
            if target >= nums[0] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # [mid, right] is sorted.
            if target > nums[mid] and target <= nums[len(nums)-1]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


"""
Leetcode link: https://leetcode.cn/problems/search-rotate-array-lcci/
Given a sorted array of n integers that has been rotated an unknown number of
times, write code to find an element in the array. You may assume that the
array was originally sorted in increasing order. If there are more than one
target elements in the array, return the smallest index.

example:
Input: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
Output: 8 (the index of 5 in the array)
"""


def searchRotatedArray2(arr: list[int], target: int) -> int:
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        if arr[left] == target:
            return left
        mid = left + (right - left) // 2
        if arr[mid] == target:
            right = mid
        elif arr[0] < arr[mid]:
            if target >= arr[0] and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[0] > arr[mid]:
            if target <= arr[n-1] and target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left += 1
    return -1
