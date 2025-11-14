"""
Leetcode link: https://leetcode.cn/problems/get-kth-magic-number-lcci/
Design an algorithm to find the kth number such that the only prime factors are
3, 5, and 7. Note that 3, 5, and 7 do not have to be factors, but it should not
have any other prime factors. For example, the first several multiples would be
(in order) 1, 3, 5, 7, 9, 15, 21.

example:
Input: k = 5
Output: 9
"""


def getKthMagicNumber(k: int) -> int:
    dp = [0] * k
    dp[0] = 1
    p3, p5, p7 = 0, 0, 0

    for i in range(1, k):
        n3, n5, n7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
        dp[i] = min(n3, min(n5, n7))
        if dp[i] == n3:
            p3 += 1
        if dp[i] == n5:
            p5 += 1
        if dp[i] == n7:
            p7 += 1

    return dp[k-1]
