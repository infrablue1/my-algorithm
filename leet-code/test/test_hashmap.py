import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.hashmap import (
    canConstruct,
    isIsomorphic,
    wordPattern,
    isAnagram,
    groupAnagrams,
    twoSum,
    isHappy,
    containsNearbyDuplicate,
    longestConsecutive
)


class TestHashmap(unittest.TestCase):

    def testCanConstruct(self):
        self.assertEqual(canConstruct("a", "b"), False)
        self.assertEqual(canConstruct("aa", "ab"), False)
        self.assertEqual(canConstruct("aa", "aab"), True)

    def testIsIsomorphic(self):
        self.assertEqual(isIsomorphic("cgg", "add"), True)
        self.assertEqual(isIsomorphic("foo", "bar"), False)
        self.assertEqual(isIsomorphic("paper", "title"), True)

    def testWordPattern(self):
        self.assertEqual(wordPattern("abba", "dog cat cat dog"), True)
        self.assertEqual(wordPattern("abba", "dog cat cat fish"), False)
        self.assertEqual(wordPattern("aaaa", "dog cat cat dog"), False)

    def testIsAnagram(self):
        self.assertEqual(isAnagram("anagram", "nagaram"), True)
        self.assertEqual(isAnagram("rat", "car"), False)

    def testGroupAnagrams(self):
        self.assertEqual(groupAnagrams(
            ["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        self.assertEqual(groupAnagrams([""]), [[""]])
        self.assertEqual(groupAnagrams(["a"]), [["a"]])

    def testTwoSum(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def testIsHappy(self):
        self.assertEqual(isHappy(19), True)
        self.assertEqual(isHappy(2), False)

    def testContainsNearbyDuplicate(self):
        self.assertEqual(containsNearbyDuplicate([1, 2, 3, 1], 3), True)
        self.assertEqual(containsNearbyDuplicate([1, 0, 1, 1], 1), True)
        self.assertEqual(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)

    def testLongestConsecutive(self):
        self.assertEqual(longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
        self.assertEqual(longestConsecutive([1, 0, 1, 2]), 3)


if __name__ == '__main__':
    unittest.main()
