"""
Leetcode link: https://leetcode.cn/problems/word-ladder-ii/
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:
1. Every adjacent pair of words differs by a single letter.
2. Every si for 1 <= i <= k is in wordList. Note that beginWord does not need
to be in wordList.
3. sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all
the shortest transformation sequences from beginWord to endWord, or an empty
list if no such sequence exists. Each sequence should be returned as a list of
the words [beginWord, s1, s2, ..., sk].

example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
"log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
"""


from collections import defaultdict, deque


def findLadders2(beginWord: str, endWord: str, wordList: list[str]) -> \
        list[list[str]]:

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

    n = len(wordList)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i+1, n):
            w1, w2 = wordList[i], wordList[j]
            if isAdjustant(w1, w2):
                graph[i].append(j)
                graph[j].append(i)

    beginIndex = wordList.index(beginWord)
    endIndex = wordList.index(endWord)

    # bfs
    def bfs(beginIndex: int, endIndex: int) -> list[list[str]]:
        q = deque()
        vis = [False] * n
        q.appendleft(beginIndex)
        vis[beginIndex] = True
        prevDict = defaultdict(set)
        flag = False
        while len(q) > 0:
            qsize = len(q)
            levelIndex = set()
            for _ in range(qsize):
                index = q.pop()
                if index == endIndex:
                    flag = True
                else:
                    for nextIndex in graph[index]:
                        if not vis[nextIndex]:
                            levelIndex.add(nextIndex)
                            q.appendleft(nextIndex)
                            prevDict[nextIndex].add(index)
            # update vis
            for index in levelIndex:
                vis[index] = True

            if flag is True:
                break

        ans = []

        def backtrack(index: int, tmp: list[str]):
            if index == beginIndex:
                ans.append(tmp[::-1])
                return

            for wordIndex in prevDict[index]:
                tmp.append(wordList[wordIndex])
                backtrack(wordIndex, tmp)
                tmp.pop()

        if flag:
            backtrack(endIndex, [endWord])
        return ans

    # dfs
    def dfs(beginIndex: int, endIndex: int) -> list[list[str]]:
        vis = [False] * n
        minCount = n + 1
        paths = defaultdict(list)

        def search(wordIndex: str, count: int, tmp: list[str]):
            nonlocal minCount
            if count > minCount:
                return
            if wordIndex == endIndex:
                minCount = min(minCount, count)
                paths[count].append(tmp.copy())
                return

            for nextIndex in graph[wordIndex]:
                if not vis[nextIndex]:
                    vis[nextIndex] = True
                    tmp.append(wordList[nextIndex])
                    search(nextIndex, count + 1, tmp)
                    tmp.pop()
                    vis[nextIndex] = False

        search(beginIndex, 1, [beginWord])
        return paths[minCount]

    result1 = dfs(beginIndex, endIndex)
    result2 = bfs(beginIndex, endIndex)
    result1.sort()
    result2.sort()
    assert result1 == result2

    return result1
