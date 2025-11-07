"""
Leetcode link: https://leetcode.cn/problems/multi-search-lcci/
Given a string band an array of smaller strings T, design a method to search b
for each small string in T. Output positions of all strings in smalls that
appear in big, where positions[i] is all positions of smalls[i].

example:
Input:
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
Output:  [[1,4],[8],[],[3],[1,4,7,10],[5]]
"""


class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.index = -1

    def insert(self, word: int, index: int):
        if len(word) == 0:
            return
        node = self
        for ch in word:
            value = ord(ch) - ord('a')
            if node.child[value] is None:
                node.child[value] = Trie()
            node = node.child[value]
        node.index = index

    def search(self, word: str, beginIndex: int, ans: list[list[int]]):
        node = self
        for ch in word:
            if node.index != -1:
                ans[node.index].append(beginIndex)
            value = ord(ch) - ord('a')
            if node.child[value] is None:
                return
            node = node.child[value]
        if node.index != -1:
            ans[node.index].append(beginIndex)


def multiSearch(big: str, smalls: list[str]) -> list[list[int]]:
    root = Trie()
    for i, s in enumerate(smalls):
        root.insert(s, i)

    ans = [[] for _ in range(len(smalls))]
    for i in range(len(big)):
        root.search(big[i:len(big)], i, ans)
    return ans
