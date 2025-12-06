"""
Leetcode link: https://leetcode.cn/problems/binary-number-to-string-lcci/
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR".

example:
Input: 0.625
Output: "0.101"
"""


def printBin(num: float) -> str:
    ans = "0."
    while len(ans) <= 32 and num != 0:
        num *= 2
        digit = int(num)
        ans += str(digit)
        num -= digit
    return ans if len(ans) <= 32 else "ERROR"
