"""
Leetcode link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
You are given an array prices where prices[i] is the price of a given stock on
the ith day. Find the maximum profit you can achieve. You may complete at most
two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

example:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
3-0 = 3. Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit =
4-1 = 3.
"""


def maxProfit3(prices: list[int]) -> int:
    maxValue = max(prices)
    buy1, buy2 = -maxValue, -maxValue
    sell1, sell2 = 0, 0

    for price in prices:
        sell2 = max(sell2, price + buy2)
        buy2 = max(buy2, sell1 - price)
        sell1 = max(sell1, price + buy1)
        buy1 = max(buy1, -price)

    return sell2


"""
Leetcode link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
You are given an integer array prices where prices[i] is the price of a given
stock on the ith day, and an integer k. Find the maximum profit you can
achieve. You may complete at most k transactions: i.e. you may buy at most k
times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

example:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4),
profit = 4-2 = 2.
"""


def maxProfit4(k: int, prices: list[int]) -> int:
    n = len(prices)
    dp = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        minPirce = prices[0]
        for j in range(1, n):
            minPirce = min(minPirce, prices[j] - dp[i - 1][j - 1])
            dp[i][j] = max(dp[i][j - 1], prices[j] - minPirce)

    return dp[k][n - 1]
