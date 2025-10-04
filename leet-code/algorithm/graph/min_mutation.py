"""
Leetcode link: https://leetcode.com/problems/minimum-genetic-mutation/
A gene string can be represented by an 8-character long string, with choices
from 'A', 'C', 'G', and 'T'. Suppose we need to investigate a mutation from a
gene string startGene to a gene string endGene where one mutation is defined as
one single character changed in the gene string.
For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A
gene must be in bank to make it a valid gene string. Given the two gene strings
startGene and endGene and the gene bank bank, return the minimum number of
mutations needed to mutate from startGene to endGene. If there is no such a
mutation, return -1.
Note that the starting point is assumed to be valid, so it might not be
included in the bank.

example:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
"""

from collections import deque


def minMutation(startGene: str, endGene: str, bank: list[str]) -> int:
    # Make genes in bank unique.
    bankSet = set(bank)
    bankSet.add(startGene)
    bank = list(bankSet)

    # Link gene string to its index
    gene2index = {}
    for i in range(len(bank)):
        gene2index[bank[i]] = i

    def charDiffCount(s: str, t: str):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count

    # Build graph with gene.
    n = len(bank)
    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if charDiffCount(bank[i], bank[j]) == 1:
                graph[i][j], graph[j][i] = True, True

    # BFS
    startIndex = gene2index.get(startGene)
    endIndex = gene2index.get(endGene)
    if startIndex == -1 or endIndex == -1:
        return -1

    q = deque()
    vis = set()
    q.append(startIndex)
    count = 0
    while len(q) > 0:
        for _ in range(len(q)):
            index = q.popleft()
            if index == endIndex:
                return count
            vis.add(index)
            for i in range(n):
                if graph[index][i] and i not in vis:
                    q.append(i)
        count += 1

    return -1
