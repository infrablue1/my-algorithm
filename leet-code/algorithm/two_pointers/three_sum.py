"""
Leetcode link: https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not
matter.
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    ans = []
    first = 0

    while first < n - 2:
        while first != 0 and nums[first] == nums[first - 1]:
            first += 1
            continue

        second, third = first + 1, n - 1
        target = - nums[first]

        while second < third:
            current_sum = nums[second] + nums[third]
            if current_sum == target:
                ans.append([nums[first], nums[second], nums[third]])
                second += 1
                while second < third and nums[second] == nums[second - 1]:
                    second += 1
            elif current_sum < target:
                second += 1
            else:
                third -= 1

        first += 1

    return ans
