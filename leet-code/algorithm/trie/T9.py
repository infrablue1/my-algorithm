"""
Leetcode link: https://leetcode.cn/problems/t9-lcci/
On old cell phones, users typed on a numeric keypad and the phone would
provide a list of words that matched these numbers. Each digit mapped to a set
of 0 - 4 letters. Implement an algo­rithm to return a list of matching words,
given a sequence of digits. You are provided a list of valid words. The mapping
is shown in the diagram below:

example:
Input: num = "8733", words = ["tree", "used"]
Output: ["tree", "used"]
"""


class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False

    def insert(self, numstr: str, num2ch):
        node = self
        for num in numstr:
            s = num2ch[num]
            newNode = Trie()
            # chile could be shared
            for ch in s:
                index = ord(ch) - ord('a')
                if node.child[index] is None:
                    node.child[index] = newNode
            node = node.child[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if node.child[index] is None:
                return False
            node = node.child[index]
        return node.isEnd


def getValidT9Words(num: str, words: list[str]) -> list[str]:
    num2ch = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
              "7": "pqrs", "8": "tuv", "9": "wxyz"}
    root = Trie()
    root.insert(num, num2ch)
    ans = []
    for word in words:
        if root.search(word):
            ans.append(word)
    return ans
