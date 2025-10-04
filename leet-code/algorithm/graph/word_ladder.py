"""
Leetcode link: https://leetcode.com/problems/word-ladder/
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:
1. Every adjacent pair of words differs by a single letter.
2. Every si for 1 <= i <= k is in wordList. Note that beginWord does not need
to be in wordList.
3. sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.

example:
Input: beginWord = "hit", endWord = "cog", wordList =
["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" ->
"dog" -> cog", which is 5 words long.
"""

from collections import deque
from collections import defaultdict


def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    if beginWord not in wordSet:
        wordList.append(beginWord)

    def isAdjacent(s: str, t: str):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count == 1

    # Build graph.
    graph = defaultdict(list)
    n = len(wordList)
    for i in range(n):
        for j in range(i + 1, n):
            w1, w2 = wordList[i], wordList[j]
            if isAdjacent(w1, w2):
                graph[w1].append(w2)
                graph[w2].append(w1)

    # Use BFS.
    vis = set()
    count = 1
    q = deque()
    q.appendleft(beginWord)

    while len(q) > 0:
        for _ in range(len(q)):
            word = q.pop()
            if word == endWord:
                return count
            vis.add(word)
            for nextWord in graph[word]:
                if nextWord not in vis:
                    q.appendleft(nextWord)

        count += 1

    return 0
