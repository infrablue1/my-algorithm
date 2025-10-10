"""
Leetcode link: https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.

example:
Input: a = "11", b = "1"
Output: "100"
"""


def addBinary(a: str, b: str) -> str:
    m, n = len(a), len(b)
    i, j = m - 1, n - 1
    carry = 0
    tmp = []

    while i >= 0 or j >= 0 or carry > 0:
        x, y = 0, 0
        if i >= 0:
            x = ord(a[i]) - ord('0')
            i -= 1
        if j >= 0:
            y = ord(b[j]) - ord('0')
            j -= 1

        total = x + y + carry
        carry = total // 2
        tmp.append(str(total % 2))

    # Reverse tmp.
    return ''.join(tmp[::-1])
