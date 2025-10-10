"""
Leetcode link: https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

example:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    prev1, prev2 = 2, 1
    for i in range(2, n):
        tmp = prev1 + prev2
        prev2 = prev1
        prev1 = tmp

    return prev1
