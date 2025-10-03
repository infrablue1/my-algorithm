"""
Leetcode link: https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].
You may return the answer in any order.

example:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
be the same combination.
"""


def combine(n: int, k: int) -> list[list[int]]:
    ans = []

    def backtrack(start: int, tmp: list[int]):
        if len(tmp) == k:
            ans.append(tmp.copy())
        else:
            for i in range(start, n + 1):
                tmp.append(i)
                backtrack(i + 1, tmp)
                tmp.pop()

    backtrack(1, [])
    return ans
