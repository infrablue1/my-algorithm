"""
Leetcode link: https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the
squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

example:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""


def isHappy(n: int) -> bool:
    s = set()
    s.add(n)

    while n != 1:
        m = n
        squre_sum = 0
        while m > 0:
            squre_sum += (m % 10) ** 2
            m //= 10

        if squre_sum in s:
            return False
        s.add(squre_sum)
        n = squre_sum

    return True
