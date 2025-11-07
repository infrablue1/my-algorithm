"""
Leetcode link: https://leetcode.cn/problems/longest-word-lcci/
Given a list of words, write a program to find the longest word made of other
words in the list. If there are more than one answer, return the one that has
smallest lexicographic order. If no answer, return an empty string.

example:
Input:  ["cat","banana","dog","nana","walk","walker","dogwalker"]
Output:  "dogwalker"
Explanation:  "dogwalker" can be made of "dog" and "walker".
"""


class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if node.child[index] is None:
                node.child[index] = Trie()
            node = node.child[index]
        node.isEnd = True

    def check(self, word: str):
        if len(word) == 0:
            return True
        node = self
        for i, ch in enumerate(word):
            index = ord(ch) - ord('a')
            if node.child[index] is None:
                return False
            node = node.child[index]
            if node.isEnd and self.check(word[i+1:]):
                return True
        return False


def longestWord(words: list[str]) -> str:
    root = Trie()
    words.sort(key=lambda x: (len(x), x))
    ans = ""

    for word in words:
        if len(word) == 0:
            continue
        if root.check(word):
            if len(word) > len(ans):
                ans = word
        else:
            root.insert(word)

    return ans
