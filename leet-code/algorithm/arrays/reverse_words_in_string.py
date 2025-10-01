"""
Leetcode link: https://leetcode.com/problems/reverse-words-in-a-string/
Given an input string s, reverse the order of the words. A word is defined as a
sequence of non-space characters. The words in s will be separated by at least
one space.
Return a string of the words in reverse order concatenated by a single space.

example:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing
spaces.
"""


def reverseWords(s: str) -> str:
    n = len(s)
    lst = list(s)

    def reverse(i: int, j: int):
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    def reverseWord():
        i, j = 0, 0
        while i < n:
            while i < j or i < n and lst[i] == ' ':
                i += 1
            while j < i or j < n and lst[j] != ' ':
                j += 1
            reverse(i, j - 1)

    def cleanSpace() -> str:
        i, j = 0, 0
        while j < n:
            while j < n and lst[j] == ' ':
                j += 1
            while j < n and lst[j] != ' ':
                lst[i] = lst[j]
                i += 1
                j += 1
            while j < n and lst[j] == ' ':
                j += 1
            if j < n:
                lst[i] = ' '
                i += 1

        return lst[:i]

    reverse(0, n - 1)
    reverseWord()
    tmp_lst = cleanSpace()
    return "".join(tmp_lst)
