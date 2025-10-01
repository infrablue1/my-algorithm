"""
Leetcode link: https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

example:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.
"""


def longestConsecutive(nums: list[int]) -> int:
    s = set(nums)
    ans = 0

    for num in nums:
        if num - 1 not in s:
            length = 1

            while num + length in nums:
                length += 1
            ans = max(ans, length)

    return ans
