import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.intervals import (
    summaryRanges,
    merge,
    insert,
    findMinArrowShots
)


class TestIntervals(unittest.TestCase):

    def testSummaryRanges(self):
        self.assertEqual(summaryRanges([0, 1, 2, 4, 5, 7]),
                         ["0->2", "4->5", "7"])
        self.assertEqual(summaryRanges([0, 2, 3, 4, 6, 8, 9]),
                         ["0", "2->4", "6", "8->9"])

    def testMerge(self):
        self.assertEqual(merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
                         [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(merge([[1, 4], [4, 5]]), [[1, 5]])
        self.assertEqual(merge([[4, 7], [1, 4]]), [[1, 7]])

    def testInsert(self):
        self.assertEqual(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                                [4, 8]), [[1, 2], [3, 10], [12, 16]])

    def testFindMinArrowShots(self):
        self.assertEqual(findMinArrowShots(
            [[10, 16], [2, 8], [1, 6], [7, 12]]), 2)
        self.assertEqual(findMinArrowShots(
            [[1, 2], [3, 4], [5, 6], [7, 8]]), 4)
        self.assertEqual(findMinArrowShots(
            [[1, 2], [2, 3], [3, 4], [4, 5]]), 2)


if __name__ == '__main__':
    unittest.main()
