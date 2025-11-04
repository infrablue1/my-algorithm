"""
Leetcode link: https://leetcode.cn/problems/re-space-lcci/
Oh, no! You have accidentally removed all spaces, punctuation, and
capitalization in a lengthy document. A sentence like "I reset the computer.
It still didn't boot!" became "iresetthecomputeritstilldidntboot''. You'll deal
with the punctuation and capi­talization later; right now you need to re-insert
the spaces. Most of the words are in a dictionary but a few are not. Given a
dictionary (a list of strings) and the document (a string), design an algorithm
to unconcatenate the document in a way that minimizes the number of
unrecognized characters. Return the number of unrecognized characters.

example:
Input:
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
Output:  7
Explanation:  After unconcatenating, we got "jess looked just like tim her
brother", which containing 7 unrecognized characters.
"""


class Trie:
    def __init__(self):
        self.child: list[Trie | None] = [None] * 26
        self.isEnd: bool = False

    def insert(self, s: str):
        cur: 'Trie' = self
        for i in range(len(s) - 1, -1, -1):
            ch = ord(s[i]) - ord('a')
            if cur.child[ch] is None:
                cur.child[ch] = Trie()
            cur = cur.child[ch]
        cur.isEnd = True


def respace(dictionary: list[str], sentence: str) -> int:
    n = len(sentence)
    maxCount = n + 1
    root = Trie()
    for word in dictionary:
        root.insert(word)

    dp = [maxCount] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        cur = root
        for j in range(i, 0, -1):
            ch = ord(sentence[j - 1]) - ord('a')
            if cur.child[ch] is None:
                break
            elif cur.child[ch].isEnd:
                dp[i] = min(dp[i], dp[j - 1])
            if dp[i] == 0:
                break
            cur = cur.child[ch]

    return dp[n]
