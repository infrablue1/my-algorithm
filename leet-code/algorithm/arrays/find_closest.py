"""
Leetcode link: https://leetcode.cn/problems/find-closest-lcci/
You have a large text file containing words. Given any two different words,
find the shortest distance (in terms of number of words) between them in the
file. If the operation will be repeated many times for the same file (but
different pairs of words), can you optimize your solution?

example:
Input: words = ["I","am","a","student","from","a","university","in","a",
"city"], word1 = "a", word2 = "student"
Output: 1
"""


def findClosest(words: list[str], word1: str, word2: str) -> int:
    n = len(words)
    index1, index2 = -n, -n
    ans = n + 1
    for i, word in enumerate(words):
        if word1 == word:
            index1 = i
            ans = min(ans, i - index2)
        elif word2 == word:
            index2 = i
            ans = min(ans, i - index1)
    return ans
