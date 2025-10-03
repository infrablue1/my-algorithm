"""
Leetcode link: https://leetcode.com/problems/word-search/
Given an m x n grid of characters board and a string word, return true if word
exists in the grid. The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or vertically
neighboring. The same letter cell may not be used more than once.

example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "ABCCED"
Output: true
"""


def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    wordLength = len(word)
    vis = [[False for _ in range(n)] for _ in range(m)]

    def backtrack(x: int, y: int, index: int) -> bool:
        if index == wordLength:
            return True
        if x >= 0 and x < m and y >= 0 and y < n and \
           not vis[x][y] and board[x][y] == word[index]:
            vis[x][y] = True
            flag = backtrack(x + 1, y, index + 1) or \
                backtrack(x, y + 1, index + 1) or \
                backtrack(x - 1, y, index + 1) or \
                backtrack(x, y - 1, index + 1)
            vis[x][y] = False
            return flag
        return False

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True

    return False
