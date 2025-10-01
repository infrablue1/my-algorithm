"""
Leetcode link:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the
number of unique elements in nums.

example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of
nums being 1 and 2 respectively. It does not matter what you leave beyond the
returned k (hence they are underscores).
"""


def removeDuplicates(nums: list[int]) -> int:
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[index] = nums[i]
            index += 1

    return index


"""
Leetcode link:
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Given an integer array nums sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

example:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements
of nums being 1, 1, 2, 2 and 3 respectively. It does not matter what you leave
beyond the returned k (hence they are underscores).
"""


def removeDuplicates2(nums: list[int]) -> int:
    index = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[index-2]:
            nums[index] = nums[i]
            index += 1

    return index
