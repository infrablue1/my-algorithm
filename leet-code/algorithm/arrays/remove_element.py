"""
Leetcode link: https://leetcode.com/problems/remove-element/
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of
nums being 2. It does not matter what you leave beyond the returned k (hence
they are underscores).
"""


def removeElement(nums: list[int], val: int) -> int:
    index = 0
    for num in nums:
        if num != val:
            nums[index] = num
            index += 1

    return index

