import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.graph import (
    numIslands,
    surroundedRegions,
    calcEquation,
    canFinish,
    findOrder,
    minMutation,
)


class TestGraph(unittest.TestCase):

    def testNumIslands(self):
        grid1 = [["1", "1", "1", "1", "0"],
                 ["1", "1", "0", "1", "0"],
                 ["1", "1", "0", "0", "0"],
                 ["0", "0", "0", "0", "0"]]

        grid2 = [["1", "1", "0", "0", "0"],
                 ["1", "1", "0", "0", "0"],
                 ["0", "0", "1", "0", "0"],
                 ["0", "0", "0", "1", "1"]]

        self.assertEqual(numIslands(grid1), 1)
        self.assertEqual(numIslands(grid2), 3)

    def _testSurroundedRegions(self, grid: list[list[str]],
                               expect: list[list[int]]):
        surroundedRegions(grid)
        self.assertEqual(grid, expect)

    def testSurroundedRegions(self):
        self._testSurroundedRegions([["X", "X", "X", "X"],
                                     ["X", "O", "O", "X"],
                                     ["X", "X", "O", "X"],
                                     ["X", "O", "X", "X"]],
                                    [["X", "X", "X", "X"],
                                     ["X", "X", "X", "X"],
                                     ["X", "X", "X", "X"],
                                     ["X", "O", "X", "X"]])
        self._testSurroundedRegions([["X"]], [["X"]])

    def _testCalcEquation(self, equations: list[list[str]],
                          values: list[list[float]],
                          queries: list[list[int]],
                          expect: list[float]):
        self.assertEqual(calcEquation(equations, values, queries), expect)

    def testCalcEquation(self):
        self.assertEqual(calcEquation([["a", "b"], ["b", "c"]],
                                      [2.0, 3.0],
                                      [["a", "c"], ["b", "a"], ["a", "e"],
                                       ["a", "a"], ["x", "x"]]),
                         [6.00000, 0.50000, -1.00000, 1.00000, -1.00000])
        self.assertEqual(calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]],
                                      [1.5, 2.5, 5.0],
                                      [["a", "c"], ["c", "b"], ["bc", "cd"],
                                       ["cd", "bc"]]),
                         [3.75000, 0.40000, 5.00000, 0.20000])
        self.assertEqual(calcEquation([["a", "b"]], [0.5],
                                      [["a", "b"], ["b", "a"], ["a", "c"],
                                       ["x", "y"]]),
                         [0.50000, 2.00000, -1.00000, -1.00000])

    def testCanFinish(self):
        self.assertEqual(canFinish(2, [[1, 0]]), True)
        self.assertEqual(canFinish(2, [[1, 0], [0, 1]]), False)

    def testFindOrder(self):
        self.assertEqual(findOrder(2, [[1, 0]]), [0, 1])
        self.assertEqual(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
                         [0, 1, 2, 3])
        self.assertEqual(findOrder(1, []), [0])

    def testMinMutation(self):
        self.assertEqual(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1)
        self.assertEqual(minMutation("AACCGGTT", "AAACGGTA",
                                     ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2)


if __name__ == '__main__':
    unittest.main()
