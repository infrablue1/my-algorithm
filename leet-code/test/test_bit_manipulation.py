import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.bit_manipulation import (
    addBinary,
    reverseBits,
    hammingWeight,
    singleNumber,
    singleNumber2,
    rangeBitwiseAnd,
    isUnique,
)


class BitManipulationTest(unittest.TestCase):

    def testAddBinary(self):
        self.assertEqual(addBinary("11", "1"), "100")
        self.assertEqual(addBinary("1010", "1011"), "10101")

    def testReverseBits(self):
        self.assertEqual(reverseBits(43261596), 964176192)
        self.assertEqual(reverseBits(2147483644), 1073741822)

    def testHammingWeight(self):
        self.assertEqual(hammingWeight(11), 3)
        self.assertEqual(hammingWeight(128), 1)
        self.assertEqual(hammingWeight(2147483645), 30)

    def testSingleNumber(self):
        self.assertEqual(singleNumber([2, 2, 1]), 1)
        self.assertEqual(singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(singleNumber([1]), 1)

    def testSingleNumber2(self):
        self.assertEqual(singleNumber2([2, 2, 3, 2]), 3)
        self.assertEqual(singleNumber2([0, 1, 0, 1, 0, 1, 99]), 99)

    def testRangeBitwiseAnd(self):
        self.assertEqual(rangeBitwiseAnd(5, 7), 4)
        self.assertEqual(rangeBitwiseAnd(0, 0), 0)
        self.assertEqual(rangeBitwiseAnd(1, 2147483647), 0)

    def testIsUnique(self):
        self.assertEqual(isUnique("leetcode"), False)
        self.assertEqual(isUnique("abc"), True)


if __name__ == '__main__':
    unittest.main()
