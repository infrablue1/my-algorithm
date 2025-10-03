"""
Leetcode link: https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""


def generateParenthesis(n: int) -> list[str]:
    ans = []

    def backtrack(left: int, right: int, tmp: list[str]):
        if right == n:
            ans.append(''.join(tmp))
        else:
            if left < n:
                tmp.append('(')
                backtrack(left + 1, right, tmp)
                tmp.pop()
            if right < left:
                tmp.append(')')
                backtrack(left, right + 1, tmp)
                tmp.pop()

    backtrack(0, 0, [])
    return ans
