"""
Leetcode link: https://leetcode.cn/problems/calculator-lcci/
Given an arithmetic equation consisting of positive integers, +, -, * and /
(no paren­theses), compute the result. The expression string contains only
non-negative integers, +, -, *, / operators and empty spaces . The integer
division should truncate toward zero.

example:
Input: "3+2*2"
Output: 7
"""


def calculate(s: str) -> int:
    n = len(s)
    stk = []
    preOperator = '+'
    num = 0

    for i in range(n):
        ch = s[i]
        if ch.isdigit():
            value = ord(ch) - ord('0')
            num = num * 10 + value
        if i == n - 1 or ch in ('+', '-', '*', '/'):
            if preOperator == '+':
                stk.append(num)
            elif preOperator == '-':
                stk.append(-num)
            elif preOperator == '*':
                stk.append(stk.pop() * num)
            elif preOperator == '/':
                stk.append(int(stk.pop() / num))
            num = 0
            preOperator = ch

    return sum(stk)
