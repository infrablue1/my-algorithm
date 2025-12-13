"""
Leetcode link: https://leetcode.cn/problems/tic-tac-toe-lcci/
Design an algorithm to figure out if someone has won a game of tic-tac-toe.
Input is a string array of size N x N, including characters " ", "X" and "O",
where " " represents a empty grid.

The rules of tic-tac-toe are as follows:
Players place characters into an empty grid(" ") in turn.
The first player always place character "O", and the second one place "X".
Players are only allowed to place characters in empty grid. Replacing a
character is not allowed.
If there is any row, column or diagonal filled with N same characters, the game
ends. The player who place the last charater wins.
When there is no empty grid, the game ends.
If the game ends, players cannot place any character further.
If there is any winner, return the character that the winner used. If there's a
draw, return "Draw". If the game doesn't end and there is no winner, return
"Pending".

example:
Input:  board = ["O X"," XO","X O"]
Output:  "X"
"""


def tictactoe(board: list[str]) -> str:
    n = len(board)
    sumRow, sumCol = 0, 0
    sumLeft, sumRight = 0, 0
    hasSpace = False
    winSumX = ord('X') * n
    winSumO = ord('O') * n

    for i in range(n):
        sumRow, sumCol = 0, 0
        for j in range(0, n):
            sumRow += 0 if board[i][j] == ' ' else ord(board[i][j])
            sumCol += 0 if board[j][i] == ' ' else ord(board[j][i])
            if board[i][j] == ' ':
                hasSpace = True
        if sumRow == winSumX or sumCol == winSumX:
            return "X"
        if sumRow == winSumO or sumCol == winSumO:
            return "O"
        sumLeft += 0 if board[i][i] == ' ' else ord(board[i][i])
        sumRight += 0 if board[i][n-1-i] == ' ' else ord(board[i][n-1-i])

    if sumLeft == winSumX or sumRight == winSumX:
        return "X"
    if sumLeft == winSumO or sumRight == winSumO:
        return "O"

    return "Pending" if hasSpace else "Draw"
