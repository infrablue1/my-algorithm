"""
Leetcode link: https://leetcode.cn/problems/diving-board-lcci/
You are building a diving board by placing a bunch of planks of wood end-to-end
There are two types of planks, one of length shorter and one of length longer.
You must use exactly K planks of wood. Write a method to generate all possible
lengths for the diving board.
return all lengths in non-decreasing order.

example:
Input:
shorter = 1
longer = 2
k = 3
Output:  {3,4,5,6}
"""


def divingBoard(shorter: int, longer: int, k: int) -> list[int]:
    if k == 0:
        return []
    if shorter == longer:
        return [shorter * k]

    minValue = shorter * k
    maxValue = longer * k
    step = longer - shorter
    return list(range(minValue, maxValue + 1, step))
