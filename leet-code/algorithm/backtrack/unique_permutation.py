"""
Leetcode link: https://leetcode.cn/problems/permutation-i-lcci/
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

example:
示例 1：
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

示例 2：
 输入：S = "ab"
 输出：["ab", "ba"
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
