import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.trie import (
    longestWord,
    multiSearch,
    getValidT9Words,
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

    def testGetValidT9Words(self):
        self.assertEqual(getValidT9Words("8733", ["tree", "used"]),
                         ["tree", "used"])
        self.assertEqual(getValidT9Words("2", ["a", "b", "c", "d"]),
                         ["a", "b", "c"])


if __name__ == '__main__':
    unittest.main()
