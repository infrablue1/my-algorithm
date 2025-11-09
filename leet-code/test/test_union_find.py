import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.union_find import (
    trulyMostPopular,
)


class UnionFindTest(unittest.TestCase):

    def testTrulyMostPopular(self):
        self.assertEqual(trulyMostPopular(["John(15)", "Jon(12)", "Chris(13)",
                                           "Kris(4)", "Christopher(19)"],
                                          ["(Jon,John)", "(John,Johnny)",
                                           "(Chris,Kris)",
                                           "(Chris,Christopher)"]),
                         ["John(27)", "Chris(36)"])


if __name__ == '__main__':
    unittest.main()
