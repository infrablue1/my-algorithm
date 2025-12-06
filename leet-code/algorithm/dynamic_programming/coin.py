"""
Leetcode link: https://leetcode.cn/problems/coin-lcci/
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5
cents), and pennies (1 cent), write code to calculate the number of ways of
representing n cents. (The result may be large, so you should return it modulo
1000000007)

example:
Input: n = 5
Output: 2
Explanation: There are two ways:
5=5
5=1+1+1+1+1
"""


def waysToChange(n: int) -> int:
    M = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    coins = [25, 10, 5, 1]

    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i-coin]) % M
    return dp[n]
