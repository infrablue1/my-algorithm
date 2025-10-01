"""
Leetcode link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
You are given an array of strings tokens that represents an arithmetic
expression in a Reverse Polish Notation. Evaluate the expression. Return an
integer that represents the value of the expression.

Note that:
1. The valid operators are '+', '-', '*', and '/'.
2. Each operand may be an integer or another expression.
3. The division between two integers always truncates toward zero.
4. There will not be any division by zero.
5. The input represents a valid arithmetic expression in a reverse polish
notation.
6. The answer and all the intermediate calculations can be represented in a
32-bit integer.

example:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""


def evalRPN(tokens: list[str]) -> int:
    stk = []
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            a = stk.pop()
            b = stk.pop()
            result = 0
            if token == '+':
                result = b + a
            elif token == '-':
                result = b - a
            elif token == '*':
                result = b * a
            elif token == '/':
                result = int(b / a)
            stk.append(result)
        else:
            stk.append(int(token))

    return stk[0]
