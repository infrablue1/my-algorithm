"""
Leetcode link: https://leetcode.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    ans = []
    n = len(nums)
    vis = [False] * n

    def backtrack(tmp: list[int]):
        if len(tmp) == n:
            ans.append(tmp.copy())
        else:
            for i in range(n):
                if not vis[i]:
                    vis[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp)
                    tmp.pop()
                    vis[i] = False

    backtrack([])
    return ans
