import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.backtrack import (
    letterCombinations,
    combine,
    permute,
    combinationSum,
    generateParenthesis,
    exist,
)


class TestBacktrack(unittest.TestCase):

    def testLetterCombinations(self):
        self.assertEqual(letterCombinations("23"),
                         ["ad", "ae", "af", "bd",
                          "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(letterCombinations(""), [])
        self.assertEqual(letterCombinations("2"), ["a", "b", "c"])

    def testCombine(self):
        self.assertEqual(combine(4, 2),
                         [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
        self.assertEqual(combine(1, 1), [[1]])

    def testPermute(self):
        self.assertEqual(permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2],
                                              [2, 1, 3], [2, 3, 1],
                                              [3, 1, 2], [3, 2, 1]])
        self.assertEqual(permute([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(permute([1]), [[1]])

    def testCombinationSum(self):
        self.assertEqual(combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(combinationSum([2, 3, 5], 8),
                         [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        self.assertEqual(combinationSum([2], 1), [])

    def testGenerateParenthesis(self):
        self.assertEqual(generateParenthesis(3),
                         ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(generateParenthesis(1), ["()"])

    def testExist(self):
        self.assertEqual(exist([["A", "B", "C", "E"],
                                ["S", "F", "C", "S"],
                                ["A", "D", "E", "E"]], "ABCCED"), True)
        self.assertEqual(exist([["A", "B", "C", "E"],
                                ["S", "F", "C", "S"],
                                ["A", "D", "E", "E"]], "SEE"), True)
        self.assertEqual(exist([["A", "B", "C", "E"],
                                ["S", "F", "C", "S"],
                                ["A", "D", "E", "E"]], "ABCB"), False)


if __name__ == '__main__':
    unittest.main()
