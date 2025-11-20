"""
Leetcode link: https://leetcode.cn/problems/missing-two-lcci/
You are given an array with all the numbers from 1 to N appearing exactly once,
except for two number that is missing. How can you find the missing number in
O(N) time and 0(1) space?
You can return the missing numbers in any order.

example:
Input: [2,3]
Output: [1,4]
"""


def missingTwo(nums: list[int]) -> list[int]:
    size = len(nums)
    n = size + 2
    total = sum(nums)
    expectTotal = n * (1 + n) // 2
    towTotal = expectTotal - total
    flag = towTotal // 2
    firstNumber = flag * (1 + flag) // 2
    for num in nums:
        if num <= flag:
            firstNumber -= num

    return [firstNumber, towTotal - firstNumber]
