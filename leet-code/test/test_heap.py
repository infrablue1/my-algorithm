import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.heap import (
    findKthLargest,
    kSmallestPairs,
)


class HeapTest(unittest.TestCase):

    def testfindKthLargest(self):
        self.assertEqual(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def testKSmallestPairs(self):
        self.assertEqual(kSmallestPairs([1, 7, 11], [2, 4, 6], 3),
                         [[1, 2], [1, 4], [1, 6]])
        self.assertEqual(kSmallestPairs([1, 1, 2], [1, 2, 3], 2),
                         [[1, 1], [1, 1]])


if __name__ == '__main__':
    unittest.main()
