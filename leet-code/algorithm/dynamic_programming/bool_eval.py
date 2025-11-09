"""
Leetcode link: https://leetcode.cn/problems/boolean-evaluation-lcci/
Given a boolean expression consisting of the symbols 0 (false), 1 (true),
& (AND), | (OR), and ^ (XOR), and a desired boolean result value result,
implement a function to count the number of ways of parenthesizing the
expression such that it evaluates to result.

example:
Input: s = "1^0|0|1", result = 0
Output: 2
Explanation: Two possible parenthesizing ways are:
1^(0|(0|1))
1^((0|0)|1)
"""


def countEval(s: str, result: int) -> int:
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1 if ord(s[0]) - ord('0') == result else 0

    # dp[n][n][2]
    dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        if s[i] == '0' or s[i] == '1':
            value = ord(s[i]) - ord('0')
            dp[i][i][value] = 1

    for length in range(2, n + 1, 2):
        for i in range(0, n - length + 1, 2):
            j = i + length
            for k in range(i + 1, j, 2):
                leftResult0, leftResult1 = dp[i][k-1][0], dp[i][k-1][1]
                rightResult0, rightResult1 = dp[k+1][j][0], dp[k+1][j][1]
                if s[k] == '&':
                    # (0, 0), (0, 1), (1, 0) => 0
                    # (1, 1) => 1
                    dp[i][j][0] += leftResult0 * rightResult0 + \
                        leftResult0 * rightResult1 + leftResult1 * rightResult0
                    dp[i][j][1] += leftResult1 * rightResult1
                elif s[k] == '|':
                    # (0, 0) => 0
                    # (0, 1), (1, 0), (1, 1) => 1
                    dp[i][j][0] += leftResult0 * rightResult0
                    dp[i][j][1] += leftResult0 * rightResult1 + \
                        leftResult1 * rightResult0 + leftResult1 * rightResult1
                elif s[k] == '^':
                    # (0, 0), (1, 1) => 0
                    # (0, 1), (1, 0) => 1
                    dp[i][j][0] += leftResult0 * rightResult0 + \
                        leftResult1 * rightResult1
                    dp[i][j][1] += leftResult0 * rightResult1 + \
                        leftResult1 * rightResult0

    return dp[0][n-1][result]
