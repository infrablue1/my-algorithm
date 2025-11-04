import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.arrays import (
    mergeSortedArray,
    removeElement,
    removeDuplicates,
    removeDuplicates2,
    majorityElement,
    rotate_v1,
    rotate_v2,
    maxProfit1,
    maxProfit2,
    canJump,
    jump,
    productExceptSelf,
    canCompleteCircuit,
    romanToInt,
    intToRoman,
    lengthOfLastWord,
    longestCommonPrefix,
    reverseWords,
    strStr,
    zigzagConvert,
    candy,
    trap,
    maxSubArray,
    maxSubarraySumCircular,
    fullJustify,
    getMaxMatrix,
    subSort,
    wiggleSort,
)


class TestArrays(unittest.TestCase):

    def _testMergeSortedArray(self, nums1: list[int], m: int,
                              nums2: list[int], n: int, expect: list[int]):
        mergeSortedArray(nums1, m, nums2, n)
        self.assertEqual(nums1, expect)

    def testMergeSortedArray(self):
        self._testMergeSortedArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3,
                                   [1, 2, 2, 3, 5, 6])
        self._testMergeSortedArray([1], 1, [], 0, [1])
        self._testMergeSortedArray([0], 0, [1], 1, [1])

    def testRemoveElement(self):
        self.assertEqual(removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def testRemoveDuplicates(self):
        self.assertEqual(removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

    def testRemoveDuplicates2(self):
        self.assertEqual(removeDuplicates2([1, 1, 1, 2, 2, 3]), 5)
        self.assertEqual(removeDuplicates2([0, 0, 1, 1, 1, 1, 2, 3, 3]), 7)

    def testMajorityElement(self):
        self.assertEqual(majorityElement([3, 2, 3]), 3)
        self.assertEqual(majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def _testRotateArray(self, nums: list[int], k: int, expect: list[int]):
        input = nums.copy()
        rotate_v1(input, k)
        self.assertEqual(input, expect)
        input = nums.copy()
        rotate_v2(input, k)
        self.assertEqual(input, expect)

    def testRotateArray(self):
        self._testRotateArray([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
        self._testRotateArray([-1, 100, 3, 99], 2, [3, 99, -1, 100])

    def testMaxProfit1(self):
        self.assertEqual(maxProfit1([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(maxProfit1([7, 6, 4, 3, 1]), 0)

    def testMaxProfit2(self):
        self.assertEqual(maxProfit2([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(maxProfit2([7, 6, 4, 3, 1]), 0)
        self.assertEqual(maxProfit2([1, 2, 3, 4, 5]), 4)

    def testCanJump(self):
        self.assertEqual(canJump([2, 3, 1, 1, 4]), True)
        self.assertEqual(canJump([3, 2, 1, 0, 4]), False)

    def testJump(self):
        self.assertEqual(jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(jump([2, 3, 0, 1, 4]), 2)

    def testProductExceptSelf(self):
        self.assertEqual(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def testCanCompleteCircuit(self):
        self.assertEqual(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
                         3)
        self.assertEqual(canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)

    def testRomanToInt(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("MCMXCIV"), 1994)

    def testIntToRoman(self):
        self.assertEqual(intToRoman(3749), "MMMDCCXLIX")
        self.assertEqual(intToRoman(58), "LVIII")
        self.assertEqual(intToRoman(1994), "MCMXCIV")

    def testLengthOfLastWord(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)

    def testLongestCommonPrefix(self):
        self.assertEqual(longestCommonPrefix(["flower", "flow", "flight"]),
                         "fl")
        self.assertEqual(longestCommonPrefix(["dog", "racecar", "car"]), "")

    def testReverseWords(self):
        self.assertEqual(reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(reverseWords("  hello world  "), "world hello")
        self.assertEqual(reverseWords("a good   example"), "example good a")

    def testStrStr(self):
        self.assertEqual(strStr("sadbutsad", "sad"), 0)
        self.assertEqual(strStr("leetcode", "leeto"), -1)

    def testZigzagConvert(self):
        self.assertEqual(zigzagConvert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zigzagConvert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(zigzagConvert("A", 1), "A")

    def testCandy(self):
        self.assertEqual(candy([1, 0, 2]), 5)
        self.assertEqual(candy([1, 2, 2]), 4)

    def testTrap(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)

    def testMaxSubArray(self):
        self.assertEqual(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maxSubArray([1]), 1)
        self.assertEqual(maxSubArray([5, 4, -1, 7, 8]), 23)

    def testMaxSubarraySumCircular(self):
        self.assertEqual(maxSubarraySumCircular([1, -2, 3, -2]), 3)
        self.assertEqual(maxSubarraySumCircular([5, -3, 5]), 10)
        self.assertEqual(maxSubarraySumCircular([-3, -2, -3]), -2)

    def testfullJustify(self):
        self.assertEqual(fullJustify(["This", "is", "an", "example", "of",
                                      "text", "justification."], 16),
                         [
                            "This    is    an",
                            "example  of text",
                            "justification.  "
                         ])

        self.assertEqual(fullJustify(["What", "must", "be", "acknowledgment",
                                      "shall", "be"], 16),
                         [
                            "What   must   be",
                            "acknowledgment  ",
                            "shall be        "
                         ])
        self.assertEqual(fullJustify(["Science", "is", "what", "we",
                                      "understand", "well", "enough", "to",
                                      "explain", "to", "a", "computer.", "Art",
                                      "is", "everything", "else", "we", "do"],
                                     20),
                         [
                             "Science  is  what we",
                             "understand      well",
                             "enough to explain to",
                             "a  computer.  Art is",
                             "everything  else  we",
                             "do                  "
                         ])

    def testGetMaxMatrix(self):
        self.assertEqual(getMaxMatrix([[-1, 0], [0, -1]]), [0, 1, 0, 1])
        self.assertEqual(getMaxMatrix([[9, -8, 1, 3, -2], [-3, 7, 6, -2, 4],
                                       [6, -4, -4, 8, -7]]),
                         [0, 0, 2, 3])

    def testSubSort(self):
        self.assertEqual(subSort(
            [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def testWiggleSort(self):
        self.assertEqual(wiggleSort([5, 3, 1, 2, 3]), [5, 1, 3, 2, 3])


if __name__ == '__main__':
    unittest.main()
