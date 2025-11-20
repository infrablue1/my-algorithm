import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.enumeration import (
    masterMind,
    patternMatching,
    oneEditAway,
    printKMoves,
    compressString,
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

    def testPrintKMoves(self):
        self.assertEqual(printKMoves(0), ["R"])
        self.assertEqual(printKMoves(2), ["_X", "LX"])
        self.assertEqual(printKMoves(5), ["_U", "X_", "XX"])

    def testCompressString(self):
        self.assertEqual(compressString("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compressString("abbccd"), "abbccd")


if __name__ == '__main__':
    unittest.main()
