"""
Leetcode link: https://leetcode.cn/problems/living-people-lcci/
Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. You may assume that all
people were born between 1900 and 2000 (inclusive). If a person was alive
during any portion of that year, they should be included in that year's count.
For example, Person (birth= 1908, death= 1909) is included in the counts for
both 1908 and 1909.
If there are more than one years that have the most number of people alive,
return the smallest one.

example:
Input:
birth = [1900, 1901, 1950]
death = [1948, 1951, 2000]
Output:  1901
"""


def maxAliveYear(birth: list[int], death: list[int]) -> int:
    count = [0] * 102
    for a, b in zip(birth, death):
        count[a - 1900] += 1
        count[b + 1 - 1900] -= 1

    maxIndex, maxCount = 0, 0
    curSum = 0
    for i in range(1, 101):
        curSum += count[i]
        if curSum > maxCount:
            maxIndex = i
            maxCount = curSum

    return maxIndex + 1900
