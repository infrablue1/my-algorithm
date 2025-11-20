import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.linked_list import (
    buildLinkedList,
    buildLinkedListWithCycle,
    buildRandomList,
    linkedList2List,
    randomList2List,
    hasCycle,
    addTwoNumbers,
    mergeTwoLists,
    copyRandomList,
    reverseBetween,
    removeNthFromEnd,
    deleteDuplicates,
    rotateRight,
    partition,
    LRUCache,
    reverseKGroup,
    sortList,
    mergeKLists,
    isPalindrome,
)


class TestLinkedList(unittest.TestCase):

    def testHasCycles(self):
        self.assertEqual(hasCycle(buildLinkedListWithCycle([3, 2, 0, 4], 1)),
                         True)
        self.assertEqual(hasCycle(buildLinkedListWithCycle([1, 2], 0)), True)
        self.assertEqual(hasCycle(buildLinkedListWithCycle([1], -1)), False)

    def _testAddTwoNumbers(self, l1: list[int], l2: list[int],
                           expect: list[int]):
        list1 = buildLinkedList(l1)
        list2 = buildLinkedList(l2)
        sum_list = addTwoNumbers(list1, list2)
        self.assertEqual(linkedList2List(sum_list), expect)

    def testAddTwoNumbers(self):
        self._testAddTwoNumbers([2, 4, 3], [5, 6, 4], [7, 0, 8])
        self._testAddTwoNumbers([0], [0], [0])
        self._testAddTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9],
                                [8, 9, 9, 9, 0, 0, 0, 1])

    def _testMergeTwoLists(self, l1: list[int], l2: list[int],
                           expect: list[int]):
        list1 = buildLinkedList(l1)
        list2 = buildLinkedList(l2)
        merged_list = mergeTwoLists(list1, list2)
        self.assertEqual(linkedList2List(merged_list), expect)

    def testMergeTwoLists(self):
        self._testMergeTwoLists([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
        self._testMergeTwoLists([], [], [])
        self._testMergeTwoLists([], [0], [0])

    def _testCopyRandomList(self, input: list[list[int]],
                            expect: list[list[int]]):
        head = buildRandomList(input)
        result = copyRandomList(head)
        self.assertEqual(randomList2List(result), expect)

    def testCopyRandomList(self):
        self._testCopyRandomList(
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        self._testCopyRandomList([[1, 1], [2, 1]], [[1, 1], [2, 1]])
        self._testCopyRandomList([[3, None], [3, 0], [3, None]],
                                 [[3, None], [3, 0], [3, None]])

    def _testReverseBetween(self, input: list[int], left: int, right: int,
                            expect: list[int]):
        head = buildLinkedList(input)
        result = reverseBetween(head, left, right)
        self.assertEqual(linkedList2List(result), expect)

    def testReverseBetween(self):
        self._testReverseBetween([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
        self._testReverseBetween([5], 1, 1, [5])

    def _testRemoveNthFromEnd(self, input: list[int], n: int,
                              expect: list[int]):
        head = buildLinkedList(input)
        result = removeNthFromEnd(head, n)
        self.assertEqual(linkedList2List(result), expect)

    def testRemoveNthFromEnd(self):
        self._testRemoveNthFromEnd([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
        self._testRemoveNthFromEnd([1], 1, [])
        self._testRemoveNthFromEnd([1, 2], 1, [1])

    def _testDeleteDuplicates(self, input: list[int], expect: list[int]):
        head = buildLinkedList(input)
        result = deleteDuplicates(head)
        self.assertEqual(linkedList2List(result), expect)

    def testDeleteDuplicates(self):
        self._testDeleteDuplicates([1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
        self._testDeleteDuplicates([1, 1, 1, 2, 3], [2, 3])

    def _testRotateRight(self, input: list[int], k: int, expect: list[int]):
        head = buildLinkedList(input)
        result = rotateRight(head, k)
        self.assertEqual(linkedList2List(result), expect)

    def testRotateRight(self):
        self._testRotateRight([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
        self._testRotateRight([0, 1, 2], 4, [2, 0, 1])

    def _testPartition(self, input: list[int], x: int, expect: list[int]):
        head = buildLinkedList(input)
        result = partition(head, x)
        self.assertEqual(linkedList2List(result), expect)

    def testPartition(self):
        self._testPartition([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5])
        self._testPartition([2, 1], 2, [1, 2])

    def _testLRUCache(self, cmds: list[str], params: list[list[int]],
                      expect: list[int | None]):
        lru_cache = None
        result = []
        for cmd, param in zip(cmds, params):
            if cmd == "LRUCache":
                lru_cache = LRUCache(param[0])
                result.append(None)
            elif cmd == "put":
                lru_cache.put(param[0], param[1])
                result.append(None)
            elif cmd == "get":
                result.append(lru_cache.get(param[0]))

        self.assertEqual(result, expect)

    def testLRUCache(self):
        self._testLRUCache(["LRUCache", "put", "put", "get", "put", "get",
                            "put", "get", "get", "get"],
                           [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4],
                            [1], [3], [4]],
                           [None, None, None, 1, None, -1, None, -1, 3, 4])

    def _testReverseKGroup(self, input: list[int], k: int, expect: list[int]):
        head = buildLinkedList(input)
        result = reverseKGroup(head, k)
        self.assertEqual(linkedList2List(result), expect)

    def testReverseKGroup(self):
        self._testReverseKGroup([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])
        self._testReverseKGroup([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])

    def _testSortList(self, input: list[int], expect: list[int]):
        head = buildLinkedList(input)
        result = sortList(head)
        self.assertEqual(linkedList2List(result), expect)

    def testSortList(self):
        self._testSortList([4, 2, 1, 3], [1, 2, 3, 4])
        self._testSortList([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])
        self._testSortList([], [])

    def _testMergeKLists(self, input: list[list[int]], expect: list[int]):
        lists = []
        for values in input:
            lists.append(buildLinkedList(values))
        result = mergeKLists(lists)
        self.assertEqual(linkedList2List(result), expect)

    def testMergeKLists(self):
        self._testMergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]],
                              [1, 1, 2, 3, 4, 4, 5, 6])
        self._testMergeKLists([], [])
        self._testMergeKLists([[]], [])

    def testIsPalindrome(self):
        self.assertEqual(isPalindrome(buildLinkedList([1, 2])), False)
        self.assertEqual(isPalindrome(buildLinkedList([1, 2, 2, 1])), True)


if __name__ == '__main__':
    unittest.main()
