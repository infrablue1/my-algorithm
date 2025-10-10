"""
Leetcode link: https://leetcode.com/problems/powx-n/
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

example:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""


def myPow(x: float, n: int) -> float:
    if x == 0 or x == 1:
        return 1

    isNegative = False
    if n < 0:
        isNegative = True
        n = -n

    ans = 1
    while n > 0:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1

    if isNegative:
        ans = 1 / ans

    return ans
