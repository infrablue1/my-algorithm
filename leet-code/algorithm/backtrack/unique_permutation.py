"""
Leetcode link: https://leetcode.cn/problems/permutation-ii-lcci/
Write a method to compute all permutations of a string whose characters are not
necessarily unique. The list of permutations should not have duplicates.

example:
 Input: S = "qqe"
 Output: ["eqq","qeq","qqe"]
"""


def uniquePermutation(S: str) -> list[str]:
    ans = []
    n = len(S)
    vis = [False] * n
    chars = sorted(S)

    def backtrack(tmp: str):
        if len(tmp) == n:
            ans.append(''.join(tmp))
        else:
            for i in range(n):
                if vis[i]:
                    continue
                if i > 0 and chars[i] == chars[i-1] and not vis[i-1]:
                    continue
                tmp.append(chars[i])
                vis[i] = True
                backtrack(tmp)
                tmp.pop()
                vis[i] = False
    backtrack([])
    return ans
