import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.binary_search import (
    searchInsert,
    searchMatrix,
    findPeakElement,
    searchRotatedArray,
    searchRange,
    findRotatedMin,
)


class BinarySearchTest(unittest.TestCase):

    def testSearchInsert(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)

    def testSearchMatrix(self):
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                                       [23, 30, 34, 60]], 3), True)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                                       [23, 30, 34, 60]], 13), False)

    def testFindPeakElement(self):
        self.assertEqual(findPeakElement([1, 2, 3, 1]), 2)
        self.assertEqual(findPeakElement([1, 2, 1, 3, 5, 6, 4]), 5)

    def testSearchRotatedSortedArray(self):
        self.assertEqual(searchRotatedArray([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(searchRotatedArray([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(searchRotatedArray([1], 0), -1)

    def testSearchRange(self):
        self.assertEqual(searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(searchRange([], 0), [-1, -1])

    def testFindRotatedMin(self):
        self.assertEqual(findRotatedMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(findRotatedMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(findRotatedMin([11, 13, 15, 17]), 11)


if __name__ == '__main__':
    unittest.main()
