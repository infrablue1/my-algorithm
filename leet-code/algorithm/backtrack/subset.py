"""
Leetcode link: https://leetcode.cn/problems/power-set-lcci/
Write a method to return all subsets of a set. The elements in a set are
pairwise distinct.
Note: The result set should not contain duplicated subsets.

example:
Input:  nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)

    def dfs(tmp: list[int], start: int, ans: list[list[int]]):
        if start == n:
            ans.append(tmp.copy())
            return

        dfs(tmp, start + 1, ans)
        tmp.append(nums[start])
        dfs(tmp, start + 1, ans)
        tmp.pop()
    ans = []
    dfs([], 0, ans)
    ans.sort()
    return ans


def subsets2(nums: list[int]) -> list[list[int]]:

    n = len(nums)
    ans = []
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i & (1 << j):
                tmp.append(nums[j])
        ans.append(tmp)
    ans.sort()
    return ans
