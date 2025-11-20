"""
Leetcode link: https://leetcode.cn/problems/langtons-ant-lcci/
An ant is sitting on an infinite grid of white and black squares. It initially
faces right. All squares are white initially.
At each step, it does the following:
(1) At a white square, flip the color of the square, turn 90 degrees right
(clockwise), and move forward one unit.
(2) At a black square, flip the color of the square, turn 90 degrees left
(counter-clockwise), and move forward one unit.
Write a program to simulate the first K moves that the ant makes and print the
final board as a grid.
The grid should be represented as an array of strings, where each element
represents one row in the grid. The black square is represented as 'X', and
the white square is represented as '_', the square which is occupied by the ant
is represented as 'L', 'U', 'R', 'D', which means the left, up, right and down
orientations respectively. You only need to return the minimum matrix that is
able to contain all squares that are passed through by the ant.

example:
Input: 2
Output:
[
  "_X",
  "LX"
]
Example 3:
"""


def printKMoves(K: int) -> list[str]:
    blackPos = set()
    directions = ["R", "D", "L", "U"]
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ndirections = len(directions)
    index = 0

    x, y = 0, 0
    for _ in range(K):
        if (x, y) in blackPos:
            blackPos.remove((x, y))
            index = (index - 1 + ndirections) % ndirections
            x, y = x + steps[index][0], y + steps[index][1]
        else:
            blackPos.add((x, y))
            index = (index + 1) % ndirections
            x, y = x + steps[index][0], y + steps[index][1]

    lastx, lasty = x, y
    xmin, xmax = x, x
    ymin, ymax = y, y
    for (x, y) in blackPos:
        xmin = min(x, xmin)
        xmax = max(x, xmax)
        ymin = min(y, ymin)
        ymax = max(y, ymax)

    board = [['_' for _ in range(ymax - ymin + 1)]
             for _ in range(xmax - xmin + 1)]
    for (x, y) in blackPos:
        board[x - xmin][y - ymin] = 'X'
    board[lastx - xmin][lasty - ymin] = directions[index]
    return [''.join(tmp) for tmp in board]
