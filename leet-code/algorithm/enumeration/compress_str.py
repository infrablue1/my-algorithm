"""
Leetcode link: https://leetcode.cn/problems/compress-string-lcci/
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string. You can assume the string has
only uppercase and lowercase letters (a - z).

example:
Input: "aabcccccaaa"
Output: "a2b1c5a3"
"""


def compressString(S: str) -> str:
    n = len(S)
    if n == 0:
        return S
    tmp = []
    count = 1
    ch = S[0]
    for i in range(1, n):
        if S[i] == ch:
            count += 1
        else:
            tmp.append(ch)
            tmp.append(str(count))
            ch = S[i]
            count = 1

    tmp.append(ch)
    tmp.append(str(count))
    s = ''.join(tmp)
    if len(s) >= n:
        return S
    return s
