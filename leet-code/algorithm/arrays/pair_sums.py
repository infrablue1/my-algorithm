"""
Leetcode link: https://leetcode.cn/problems/pairs-with-sum-lcci/
Design an algorithm to find all pairs of integers within an array which sum to
a specified value.

example:
Input: nums = [5,6,5], target = 11
Output: [[5,6]]
"""


def pairSums(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    i, j = 0, n - 1
    ans = []
    while i < j:
        total = nums[i] + nums[j]
        if total == target:
            ans.append([nums[i], nums[j]])
            i += 1
            j -= 1
        elif total < target:
            i += 1
        elif total > target:
            j -= 1

    return ans
