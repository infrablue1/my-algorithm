"""
Leetcode link: https://leetcode.com/problems/basic-calculator/
Given a string s representing a valid expression, implement a basic calculator
to evaluate it, and return the result of the evaluation.

example:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


def calculate(s: str) -> int:
    n = len(s)
    stk = []
    i = 0
    result, sign = 0, 1

    while i < n:
        if s[i].isdigit():
            tmp = int(s[i])
            while i + 1 < n and s[i + 1].isdigit():
                tmp = tmp * 10 + int(s[i + 1])
                i += 1
            result += sign * tmp
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            # Push current result and sign of this ()
            stk.append(result)
            stk.append(sign)
            result, sign = 0, 1
        elif s[i] == ')':
            # The stack top is the sign value of current () 
            result = result * stk.pop() + stk.pop()

        i += 1

    return result
