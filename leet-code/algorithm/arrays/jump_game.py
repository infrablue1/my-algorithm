"""
Leetcode link: https://leetcode.com/problems/jump-game/
You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum
jump length at that position.
Return true if you can reach the last index, or false otherwise.

example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


def canJump(nums: list[int]) -> bool:
    n = len(nums)
    pos = n - 1
    i = n - 2

    while i >= 0:
        if nums[i] + i >= pos:
            pos = i
        i -= 1

    return pos == 0


"""
Leetcode link: https://leetcode.com/problems/jump-game-ii/
You are given a 0-indexed array of integers nums of length n. You are initially
positioned at index 0. Each element nums[i] represents the maximum length of a
forward jump from index i. In other words, if you are at index i, you can jump
to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach index n - 1. The test cases are
generated such that you can reach index n - 1.

example:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
step from index 0 to 1, then 3 steps to the last index.
"""


def jump(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    count = 1
    left, right = 0, nums[0]

    while right < n - 1:
        right_most = max(i + nums[i] for i in range(left, right + 1))
        left, right = right + 1, right_most
        count += 1

    return count
