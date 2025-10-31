import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.coordinate_geometry import (
    cutSquares,
    bestLine
)


class CoordinateGeometryTest(unittest.TestCase):

    def testCutSquares(self):
        self.assertEqual(cutSquares([-1, -1, 2], [0, -1, 2]), [-1, 0, 2, 0])

    def testBestLine(self):
        self.assertEqual(bestLine([[0, 0], [1, 1], [1, 0], [2, 0]]), [0, 2])


if __name__ == '__main__':
    unittest.main()
