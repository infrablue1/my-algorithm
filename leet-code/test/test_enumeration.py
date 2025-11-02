import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.enumeration import (
    masterMind,
    patternMatching,
    oneEditAway,
)


class TestBruteForce(unittest.TestCase):

    def testMasterMind(self):
        self.assertEqual(masterMind("RGBY", "GGRR"), [1, 1])

    def testPatternMatching(self):
        self.assertEqual(patternMatching("abba", "dogcatcatdog"), True)
        self.assertEqual(patternMatching("abba", "dogcatcatfish"), False)
        self.assertEqual(patternMatching("aaaa", "dogcatcatdog"), False)
        self.assertEqual(patternMatching("abba", "dogdogdogdog"), True)

    def testOneEditAway(self):
        self.assertEqual(oneEditAway("pale", "ple"), True)
        self.assertEqual(oneEditAway("pales", "pal"), False)


if __name__ == '__main__':
    unittest.main()
