"""
Leetcode link: https://leetcode.com/problems/interleaving-string/
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2. An interleaving of two strings s and t is a configuration where s
and t are divided into n and m substrings respectively, such that:
1. s = s1 + s2 + ... + sn
2. t = t1 + t2 + ... + tm
3. |n - m| <= 1
4. The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2
+ t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

example:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" =
"aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n, p = len(s1), len(s2), len(s3)
    if m + n != p:
        return False

    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            index = i + j - 1
            dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[index] or \
                dp[i][j - 1] and s2[j - 1] == s3[index]

    return dp[m][n]
