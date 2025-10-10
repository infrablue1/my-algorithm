import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.math import (
    isPalindrome,
    plusOne,
    trailingZeroes,
    mySqrt,
    myPow,
)


class MathTest(unittest.TestCase):

    def testIsPalindrome(self):
        self.assertEqual(isPalindrome(121), True)
        self.assertEqual(isPalindrome(-121), False)
        self.assertEqual(isPalindrome(10), False)

    def testPlusOne(self):
        self.assertEqual(plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(plusOne([9]), [1, 0])

    def testTrailingZeroes(self):
        self.assertEqual(trailingZeroes(3), 0)
        self.assertEqual(trailingZeroes(5), 1)
        self.assertEqual(trailingZeroes(0), 0)

    def testMySqrt(self):
        self.assertEqual(mySqrt(4), 2)
        self.assertEqual(mySqrt(8), 2)

    def testMyPow(self):
        self.assertEqual(myPow(2.0, 10), 1024.0)
        self.assertEqual(round(myPow(2.1, 3), 2), 9.26)
        self.assertEqual(myPow(2.0, -2), 0.25)


if __name__ == '__main__':
    unittest.main()
