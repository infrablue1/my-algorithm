"""
Leetcode link: https://leetcode.cn/problems/sparse-array-search-lcci/
Given a sorted array of strings that is interspersed with empty strings, write
a method to find the location of a given string.

example:
 Input: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "",
 ""], s = "ta"
 Output: -1
 Explanation: Return -1 if s is not in words.
"""


def sparseSearch(words: list[str], s: str) -> int:
    n = len(words)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        while mid > left and words[mid] == "":
            mid -= 1
        if s == words[mid]:
            return mid

        if s < words[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1
