"""
Leetcode link: https://leetcode.cn/problems/rank-from-stream-lcci/
Imagine you are reading in a stream of integers. Periodically, you wish to be
able to look up the rank of a number x (the number of values less than or equal
to x). lmplement the data structures and algorithms to support these operations
. That is, implement the method track (int x), which is called when each number
is generated, and the method getRankOfNumber(int x), which returns the number
of values less than or equal to x.

example:
Input:
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
Output:
[null,0,null,1]
"""


class StreamRank:

    def __init__(self):
        self.nums = []

    def track(self, x: int) -> None:
        index = self.getRankOfNumber(x)
        self.nums.insert(index, x)

    # Upper bound
    def getRankOfNumber(self, x: int) -> int:
        n = len(self.nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if self.nums[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left
