"""
Leetcode link: https://leetcode.cn/problems/find-longest-subarray-lcci/
Given an array filled with letters and numbers, find the longest subarray with
an equal number of letters and numbers. Return the subarray. If there are more
than one answer, return the one which has the smallest index of its left
endpoint. If there is no answer, return an empty arrary.

example:
Input: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J",
"K","L","M"]
Output: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
"""


def findLongestSubarray(array: list[str]) -> list[str]:
    prefixSum = {0: -1}
    total = 0
    maxLength = 0
    startIndex = -1

    for i, s in enumerate(array):
        if s[0].isdigit():
            total += 1
        else:
            total -= 1
        if total in prefixSum:
            prevIndex = prefixSum[total]
            curLen = i - prevIndex - 1
            if curLen > maxLength:
                maxLength = curLen
                startIndex = prevIndex + 1
        else:
            prefixSum[total] = i

    if maxLength == 0:
        return []
    return array[startIndex:startIndex + maxLength + 1]
