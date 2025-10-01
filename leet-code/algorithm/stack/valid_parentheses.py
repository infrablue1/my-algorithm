"""
Leetcode link: https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

example:
Input: s = "()[]{}"
Output: true
"""


def isValid(s: str) -> bool:
    paren_dict = {'(': ')', '[': ']', '{': '}'}
    stk = []

    for c in s:
        if c in paren_dict.keys():
            stk.append(c)
        else:
            if len(stk) == 0 or paren_dict[stk.pop()] != c:
                return False

    return len(stk) == 0
