"""
Leetcode link: https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    num2index = {}
    ans = []
    for i in range(len(nums)):
        expect = target - nums[i]
        if expect in num2index:
            ans = [i, num2index[expect]]
            break

        num2index[nums[i]] = i

    ans.sort()
    return ans
