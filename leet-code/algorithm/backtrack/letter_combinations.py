"""
Leetcode link:
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


def letterCombinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    numberDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                  '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = []
    n = len(digits)

    def backtrack(startIdx: int, tmp: str) -> None:
        if len(tmp) == n:
            ans.append(tmp)
        else:
            number = digits[startIdx]
            s = numberDict[number]
            for ch in s:
                backtrack(startIdx + 1, tmp + ch)

    backtrack(0, "")
    return ans
