"""
Leetcode link: https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:

example:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


def zigzagConvert(s: str, numRows: int) -> str:
    n = len(s)
    tmp = [[] for _ in range(numRows)]
    i = 0

    while i < n:
        count = 0
        while i < n and count < numRows:
            tmp[count].append(s[i])
            i += 1
            count += 1

        count = 0
        while i < n and count < numRows - 2:
            idx = numRows - 2 - count
            tmp[idx].append(s[i])
            i += 1
            count += 1

    ans = ""
    for lst in tmp:
        ans += "".join(lst)

    return ans
