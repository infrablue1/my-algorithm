"""
Leetcode link: https://leetcode.cn/problems/shortest-supersequence-lcci/
You are given two arrays, one shorter (with all distinct elements) and one
longer. Find the shortest subarray in the longer array that contains all the
elements in the shorter array. The items can appear in any order. Return the
indexes of the leftmost and the rightmost elements of the array. If there are
more than one answer, return the one that has the smallest left index. If there
is no answer, return an empty array.

example:
Input:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
Output: [7,10]
"""


def shortestSeq(big: list[int], small: list[int]) -> list[int]:
    countMap = {}
    for num in small:
        countMap[num] = countMap.get(num, 0) + 1
    need = len(small)
    n = len(big)
    left = 0
    minStart = 0
    minLen = n + 1

    for right in range(n):
        num = big[right]
        if num in countMap:
            if countMap[num] > 0:
                need -= 1
            countMap[num] -= 1

        while need == 0 and left < n:
            tmpLen = right - left + 1
            tmpStart = left
            if tmpLen < minLen:
                minLen = tmpLen
                minStart = tmpStart
            num = big[left]
            if num in countMap:
                if countMap[num] >= 0:
                    need += 1
                countMap[num] += 1
            left += 1
    return [] if minLen == n + 1 else [minStart, minStart + minLen - 1]
