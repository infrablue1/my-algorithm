"""
Leetcode link: https://leetcode.cn/problems/circus-tower-lcci/
A circus is designing a tower routine consisting of people standing atop on
anoth­er's shoulders. For practical and aesthetic reasons, each person must
be both shorter and lighter than the person below him or her. Given the
heights and weights of each person in the circus, write a method to compute
the largest possible number of people in such a tower.

example:
Input: height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
Output: 6
Explanation: The longest tower is length 6 and includes from top to bottom:
(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
"""


def bestSeqAtIndex(height: list[int], weight: list[int]) -> int:
    pairs = list(zip(height, weight))
    pairs.sort(key=lambda x: (x[0], -x[1]))

    n = len(pairs)
    size = 0
    tails = [(0, 0)] * n
    for pair in pairs:
        i, j = 0, size
        while i < j:
            mid = i + (j - i) // 2
            if tails[mid][1] < pair[1]:
                i = mid + 1
            else:
                j = mid
        tails[i] = pair
        size = max(i + 1, size)

    return size
