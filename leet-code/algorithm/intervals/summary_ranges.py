"""
Leetcode link: https://leetcode.com/problems/summary-ranges/
You are given a sorted unique integer array nums. A range [a,b] is the set of
all integers from a to b (inclusive). Return the smallest sorted list of ranges
that cover all the numbers in the array exactly. That is, each element of nums
is covered by exactly one of the ranges, and there is no integer x such that x
is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
1. "a->b" if a != b
2. "a" if a == b

example:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7
"""


def summaryRanges(nums: list[int]) -> list[str]:
    if len(nums) == 0:
        return []

    def range2str(start: int, end: int) -> str:
        if start == end:
            return str(start)
        return f"{start}->{end}"

    ans = []
    start = 0
    for end in range(1, len(nums)):
        if nums[end] - 1 != nums[end - 1]:
            ans.append(range2str(nums[start], nums[end - 1]))
            start = end

    # Append last interval.
    ans.append(range2str(nums[start], nums[-1]))
    return ans
