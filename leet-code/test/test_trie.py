import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.trie import (
    longestWord,
    multiSearch,
)


class TrieTest(unittest.TestCase):

    def testLongestWord(self):
        self.assertEqual(longestWord(["cat", "banana", "dog", "nana", "walk",
                                      "walker", "dogwalker"]), "dogwalker")

    def testMultiSearch(self):
        self.assertEqual(multiSearch("mississippi",
                                     ["is", "ppi", "hi", "sis", "i",
                                      "ssippi"]),
                         [[1, 4], [8], [], [3], [1, 4, 7, 10], [5]])


if __name__ == '__main__':
    unittest.main()
