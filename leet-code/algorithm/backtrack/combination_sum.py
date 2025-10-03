"""
Leetcode link: https://leetcode.com/problems/combination-sum/
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
times. 7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    n = len(candidates)
    ans = []

    def backtrack(start: int, total: int, tmp: list[int]):
        if start >= n or total > target:
            return
        if total == target:
            ans.append(tmp.copy())
        else:
            for i in range(start, n):
                tmp.append(candidates[i])
                backtrack(i, total + candidates[i], tmp)
                tmp.pop()

    backtrack(0, 0, [])
    return ans
