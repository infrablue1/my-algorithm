import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.divide_conqure import (
    hanota,
)


class TestDivideConqure(unittest.TestCase):

    def testHanota(self):
        self.assertEqual(hanota([2, 1, 0], [], []), [2, 1, 0])
        self.assertEqual(hanota([1, 0], [], []), [1, 0])


if __name__ == '__main__':
    unittest.main()
