import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.two_pointers import (
    isPalindrome,
    isSubsequence,
    twoSum2,
    maxArea,
    threeSum
)


class TestTwoPointers(unittest.TestCase):

    def testIsPalindrome(self):
        self.assertEqual(isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(isPalindrome("race a car"), False)
        self.assertEqual(isPalindrome(" "), True)

    def testIsSubsequence(self):
        self.assertEqual(isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(isSubsequence("axc", "ahbgdc"), False)

    def testTwoSum2(self):
        self.assertEqual(twoSum2([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(twoSum2([2, 3, 4], 6), [1, 3])
        self.assertEqual(twoSum2([-1, 0], -1), [1, 2])

    def testMaxArea(self):
        self.assertEqual(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(maxArea([1, 1]), 1)

    def testThreeSum(self):
        self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]),
                         [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(threeSum([0, 1, 1]), [])
        self.assertEqual(threeSum([0, 0, 0]), [[0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
