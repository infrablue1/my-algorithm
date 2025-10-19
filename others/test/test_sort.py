import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from sort import (
    insertSort,
    bubbleSort,
    quickSort,
    mergeSort,
    heapSort,
    radixSort,
)


class TestSort(unittest.TestCase):

    def testInsertSort(self):
        self.assertEqual(insertSort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(insertSort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(insertSort([1]), [1])

    def testBubbleSort(self):
        self.assertEqual(bubbleSort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(bubbleSort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(bubbleSort([1]), [1])

    def testQuickSort(self):
        self.assertEqual(quickSort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(quickSort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(quickSort([1]), [1])

    def testMergeSort(self):
        self.assertEqual(mergeSort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(mergeSort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(mergeSort([1]), [1])

    def testHeapSort(self):
        self.assertEqual(heapSort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(heapSort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(heapSort([1]), [1])

    def testRadixSort(self):
        self.assertEqual(radixSort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(radixSort([170, 45, 75, 90, 802, 24, 2, 66]),
                         [2, 24, 45, 66, 75, 90, 170, 802])


if __name__ == '__main__':
    unittest.main()
