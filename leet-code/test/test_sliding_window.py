import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.sliding_window import (
    minSubArrayLen,
    lengthOfLongestSubstring,
    findSubstring,
    minWindow,
    shortestSeq,
)


class TestSlidingWindow(unittest.TestCase):

    def testMinSubArrayLen(self):
        self.assertEqual(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
        self.assertEqual(minSubArrayLen(4, [1, 4, 4]), 1)
        self.assertEqual(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)

    def testLlengthOfLongestSubstring(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

    def testFindSubstring(self):
        self.assertEqual(findSubstring("barfoothefoobarman", ["foo", "bar"]),
                         [0, 9])
        self.assertEqual(findSubstring("wordgoodgoodgoodbestword",
                                       ["word", "good", "best", "word"]), [])
        self.assertEqual(findSubstring("barfoofoobarthefoobarman",
                                       ["bar", "foo", "the"]), [6, 9, 12])

    def testMinWindow(self):
        self.assertEqual(minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minWindow("a", "a"), "a")
        self.assertEqual(minWindow("a", "aa"), "")

    def testShortestSeq(self):
        self.assertEqual(shortestSeq([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8,
                                      8, 9, 7], [1, 5, 9]), [7, 10])
        self.assertEqual(shortestSeq([1, 2, 3], [4]), [])


if __name__ == '__main__':
    unittest.main()
