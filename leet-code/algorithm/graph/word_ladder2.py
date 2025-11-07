"""
Leetcode link: https://leetcode.cn/problems/word-transformer-lcci/
Given two words of equal length that are in a dictionary, write a method to
transform one word into another word by changing only one letter at a time. The
new word you get in each step must be in the dictionary. Write code to return a
possible transforming sequence. If there is more than one sequence, return any
of them.

example:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
["hit","hot","dot","lot","log","cog"]
"""


from collections import defaultdict, deque


def findLadders(beginWord: str, endWord: str, wordList: list[str]) \
        -> list[str]:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    wordSet.add(beginWord)
    wordList = list(wordSet)

    def isAdjustant(w1: str, w2: str) -> bool:
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count == 1

    # Note: sort wordList is only for result to be deterministic,
    # which is not deterministic.
    wordList.sort()

    n = len(wordList)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i+1, n):
            w1, w2 = wordList[i], wordList[j]
            if isAdjustant(w1, w2):
                graph[i].append(j)
                graph[j].append(i)

    # bfs
    beginIndex = wordList.index(beginWord)
    endIndex = wordList.index(endWord)
    q = deque()
    vis = [False] * n
    q.appendleft(beginIndex)
    vis[beginIndex] = True
    prevDict = {}
    flag = False
    while len(q) > 0:
        index = q.pop()
        if index == endIndex:
            flag = True
            break
        for nextIndex in graph[index]:
            if vis[nextIndex] is False:
                vis[nextIndex] = True
                q.appendleft(nextIndex)
                prevDict[nextIndex] = index

    ans = []
    if flag:
        index = endIndex
        while index != beginIndex:
            ans.append(wordList[index])
            index = prevDict[index]
        ans.append(wordList[beginIndex])
        ans.reverse()

    return ans
