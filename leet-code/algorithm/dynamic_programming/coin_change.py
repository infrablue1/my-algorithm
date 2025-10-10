"""
Leetcode link: https://leetcode.com/problems/coin-change/
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""


def coinChange(coins: list[int], amount: int) -> int:
    maxValue = amount + 1
    dp = [0] + [maxValue] * amount
    coins.sort()

    for i in range(1, amount + 1):
        for coin in coins:
            j = i - coin
            if j >= 0:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[amount] if dp[amount] != maxValue else -1
