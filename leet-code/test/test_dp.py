import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.dynamic_programming import (
    climbStairs,
    rob,
    wordBreak,
    coinChange,
    lengthOfLIS,
    minimumTotal,
    minPathSum,
    uniquePathsWithObstacles,
    longestPalindrome,
    isInterleave,
)


class DPTest(unittest.TestCase):

    def testClimbStaris(self):
        self.assertEqual(climbStairs(2), 2)
        self.assertEqual(climbStairs(3), 3)

    def testRob(self):
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)

    def testWordBreak(self):
        self.assertEqual(wordBreak("leetcode", ["leet", "code"]), True)
        self.assertEqual(wordBreak("applepenapple", ["apple", "pen"]), True)
        self.assertEqual(wordBreak(
            "catsandog", ["cats", "dog", "sand", "and", "cat"]), False)

    def testCoinChange(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)
        self.assertEqual(coinChange([2], 3), -1)
        self.assertEqual(coinChange([1], 0), 0)

    def testlengthOfLIS(self):
        self.assertEqual(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def testMinimumTotal(self):
        self.assertEqual(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]),
                         11)
        self.assertEqual(minimumTotal([[-10]]), -10)

    def testMinPathSum(self):
        self.assertEqual(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        self.assertEqual(minPathSum([[1, 2, 3], [4, 5, 6]]), 12)

    def testUniquePathsWithObstacles(self):
        self.assertEqual(uniquePathsWithObstacles(
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
        self.assertEqual(uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)

    def testLongestPalindrome(self):
        self.assertEqual(longestPalindrome("babad"), "bab")
        self.assertEqual(longestPalindrome("cbbd"), "bb")

    def testIsInterleave(self):
        self.assertEqual(isInterleave("aabcc", "dbbca", "aadbbcbcac"), True)
        self.assertEqual(isInterleave("aabcc", "dbbca", "aadbbbaccc"), False)
        self.assertEqual(isInterleave("", "", ""), True)


if __name__ == '__main__':
    unittest.main()
