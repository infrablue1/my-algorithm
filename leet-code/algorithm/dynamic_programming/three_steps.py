"""
Leetcode link: https://leetcode.cn/problems/three-steps-problem-lcci/
A child is running up a staircase with n steps and can hop either 1 step, 2
steps, or 3 steps at a time. Implement a method to count how many possible ways
the child can run up the stairs. The result may be large, so return it modulo
1000000007.

example:
Input: n = 3
Output: 4
"""


def waysToStep(n: int) -> int:
    prev1, prev2, prev3 = 4, 2, 1

    if n == 1:
        return prev3
    elif n == 2:
        return prev2
    elif n == 3:
        return prev1

    for i in range(3, n):
        tmp = (prev1 + prev2 + prev3) % 1000000007
        prev3 = prev2
        prev2 = prev1
        prev1 = tmp
    return prev1
