import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.matrix import (
    isValidSudoku,
    spiralOrder,
    rotate,
    setZeroes,
    gameOfLife
)

BOARD1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

BOARD2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


class TestMatrix(unittest.TestCase):

    def testIsValidSudoku(self):
        self.assertEqual(isValidSudoku(BOARD1), True)
        self.assertEqual(isValidSudoku(BOARD2), False)

    def testSpiralOrder(self):
        self.assertEqual(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8],
                                      [9, 10, 11, 12]]),
                         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    def _testRotate(self, input: list[list[int]], expect: list[list[int]]):
        rotate(input)
        self.assertEqual(input, expect)

    def testRotate(self):
        self._testRotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                         [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        self._testRotate([[5, 1, 9, 11], [2, 4, 8, 10],
                          [13, 3, 6, 7], [15, 14, 12, 16]],
                         [[15, 13, 2, 5], [14, 3, 4, 1],
                          [12, 6, 8, 9], [16, 7, 10, 11]])

    def _testZeros(self, matrix: list[list[int]], expect: list[list[int]]):
        setZeroes(matrix)
        self.assertEqual(matrix, expect)

    def testZeros(self):
        self._testZeros([[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                        [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        self._testZeros([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def _testGameOfLife(self, board: list[list[int]], expect: list[list[int]]):
        gameOfLife(board)
        self.assertEqual(board, expect)

    def testGameOfLife(self):
        self._testGameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
                             [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
        self._testGameOfLife([[1, 1], [1, 0]], [[1, 1], [1, 1]])


if __name__ == '__main__':
    unittest.main()
