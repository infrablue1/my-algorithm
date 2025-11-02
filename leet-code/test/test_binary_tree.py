import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.binary_tree import (
    buildBinaryTree,
    binaryTree2List,
    binaryTree2ListWithNext,
    findNode,
    maxDepth,
    isSameTree,
    invertTree,
    isSymmetric,
    buildTreeFromPreorderInorder,
    buildTreeFromInorderPostOrder,
    connect,
    flatten,
    hasPathSum,
    maxPathSum,
    pathSum,
    sumNumbers,
    countNodes,
    lowestCommonAncestor,
    rightSideView,
    averageOfLevels,
    levelOrder,
    zigzagLevelOrder,
    getMinimumDifference,
    kthSmallest,
    isValidBST,
)


class TestBinaryTree(unittest.TestCase):

    def testMaxDepth(self):
        self.assertEqual(maxDepth(
            buildBinaryTree([3, 9, 20, None, None, 15, 7])), 3)
        self.assertEqual(maxDepth(buildBinaryTree([1, None, 2])), 2)

    def _testIsSameTree(self, p: list[int | None],
                        q: list[int | None], expect: bool):
        root1 = buildBinaryTree(p)
        root2 = buildBinaryTree(q)
        self.assertEqual(isSameTree(root1, root2), expect)

    def testIsSameTree(self):
        self._testIsSameTree([1, 2, 3], [1, 2, 3], True)
        self._testIsSameTree([1, 2], [1, None, 2], False)
        self._testIsSameTree([1, 2, 1], [1, 1, 2], False)

    def _testInvertTree(self, values: list[int], expect: list[int]):
        root = buildBinaryTree(values)
        root = invertTree(root)
        self.assertEqual(binaryTree2List(root), expect)

    def testInvertTree(self):
        self._testInvertTree([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])
        self._testInvertTree([2, 1, 3], [2, 3, 1])
        self._testInvertTree([], [])

    def testIsSymmetric(self):
        self.assertEqual(isSymmetric(buildBinaryTree([1, 2, 2, 3, 4, 4, 3])),
                         True)
        self.assertEqual(isSymmetric(
            buildBinaryTree([1, 2, 2, None, 3, None, 3])), False)

    def _testBuildTreeFromPreorderInorder(self, preorder: list[int],
                                          inorder: list[int],
                                          expect: list[int]):
        root = buildTreeFromPreorderInorder(preorder, inorder)
        self.assertEqual(binaryTree2List(root), expect)

    def testBuildTreeFromPreorderInorder(self):
        self._testBuildTreeFromPreorderInorder([3, 9, 20, 15, 7],
                                               [9, 3, 15, 20, 7],
                                               [3, 9, 20, None, None, 15, 7])
        self._testBuildTreeFromPreorderInorder([-1], [-1], [-1])

    def _testBuildTreeFromInorderPostOrder(self, inorder: list[int],
                                           postorder: list[int],
                                           expect: list[int]):
        root = buildTreeFromInorderPostOrder(inorder, postorder)
        self.assertEqual(binaryTree2List(root), expect)

    def testBuildTreeFromInorderPostOrder(self):
        self._testBuildTreeFromInorderPostOrder([9, 3, 15, 20, 7],
                                                [9, 15, 7, 20, 3],
                                                [3, 9, 20, None, None, 15, 7])
        self._testBuildTreeFromInorderPostOrder([-1], [-1], [-1])

    def _testConnect(self, values: list[int], expect: list[int | str]):
        root = buildBinaryTree(values)
        self.assertEqual(binaryTree2ListWithNext(connect(root)), expect)

    def testConnect(self):
        self._testConnect([1, 2, 3, 4, 5, None, 7],
                          [1, '#', 2, 3, '#', 4, 5, 7, '#'])
        self._testConnect([], [])

    def _testFlatten(self, values: list[int | None], expect: list[int | None]):
        root = buildBinaryTree(values)
        flatten(root)
        self.assertEqual(binaryTree2List(root), expect)

    def testFlatten(self):
        self._testFlatten([1, 2, 5, 3, 4, None, 6],
                          [1, None, 2, None, 3, None, 4, None, 5, None, 6])
        self._testFlatten([], [])
        self._testFlatten([0], [0])

    def testHasPathSum(self):
        self.assertEqual(hasPathSum(buildBinaryTree(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22), True)
        self.assertEqual(hasPathSum(buildBinaryTree([1, 2, 3]), 5), False)
        self.assertEqual(hasPathSum(buildBinaryTree([]), 0), False)

    def testSumNumbers(self):
        self.assertEqual(sumNumbers(buildBinaryTree([1, 2, 3])), 25)
        self.assertEqual(sumNumbers(buildBinaryTree([4, 9, 0, 5, 1])), 1026)

    def testCountNodes(self):
        self.assertEqual(countNodes(buildBinaryTree([1, 2, 3, 4, 5, 6])), 6)
        self.assertEqual(countNodes(buildBinaryTree([])), 0)
        self.assertEqual(countNodes(buildBinaryTree([1])), 1)

    def _testLowestCommonAncestor(self, values: list[int | None],
                                  p: int, q: int, expect: int):
        root = buildBinaryTree(values)
        pnode, qnode = findNode(root, p), findNode(root, q)
        result = lowestCommonAncestor(root, pnode, qnode)
        self.assertEqual(result.val, expect)

    def testLowestCommonAncestor(self):
        self._testLowestCommonAncestor([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
                                       5, 1, 3)
        self._testLowestCommonAncestor([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
                                       5, 4, 5)
        self._testLowestCommonAncestor([1, 2], 1, 2, 1)

    def testMaxPathSum(self):
        self.assertEqual(maxPathSum(buildBinaryTree([1, 2, 3])), 6)
        self.assertEqual(maxPathSum(buildBinaryTree(
            [-10, 9, 20, None, None, 15, 7])), 42)

    def _testRightSideView(self, values: list[int | None],
                           expect: list[int | None]):
        root = buildBinaryTree(values)
        result = rightSideView(root)
        self.assertEqual(result, expect)

    def testRightSideView(self):
        self._testRightSideView([1, 2, 3, None, 5, None, 4], [1, 3, 4])
        self._testRightSideView([1, 2, 3, 4, None, None, None, 5],
                                [1, 3, 4, 5])
        self._testRightSideView([1, None, 3], [1, 3])
        self._testRightSideView([], [])

    def _testAverageOfLevels(self, values: list[int | None],
                             expect: list[float]):
        root = buildBinaryTree(values)
        result = averageOfLevels(root)
        self.assertEqual(result, expect)

    def testAverageOfLevels(self):
        self._testAverageOfLevels([3, 9, 20, None, None, 15, 7],
                                  [3.00000, 14.50000, 11.00000])
        self._testAverageOfLevels([3, 9, 20, 15, 7],
                                  [3.00000, 14.50000, 11.00000])

    def _testLevelOrder(self, values: list[int | None],
                        expect: list[list[int]]):
        root = buildBinaryTree(values)
        result = levelOrder(root)
        self.assertEqual(result, expect)

    def testLevelOrder(self):
        self._testLevelOrder([3, 9, 20, None, None, 15, 7],
                             [[3], [9, 20], [15, 7]])
        self._testLevelOrder([1], [[1]])
        self._testLevelOrder([], [])

    def _testZigzagLevelOrder(self, values: list[int | None],
                              expect: list[list[int]]):
        root = buildBinaryTree(values)
        result = zigzagLevelOrder(root)
        self.assertEqual(result, expect)

    def testZigzagLevelOrder(self):
        self._testZigzagLevelOrder([3, 9, 20, None, None, 15, 7],
                                   [[3], [20, 9], [15, 7]])
        self._testZigzagLevelOrder([1], [[1]])
        self._testZigzagLevelOrder([], [])

    def testGetMinimumDifference(self):
        self.assertEqual(getMinimumDifference(buildBinaryTree(
            [4, 2, 6, 1, 3])), 1)
        self.assertEqual(getMinimumDifference(buildBinaryTree(
            [1, 0, 48, None, None, 12, 49])), 1)

    def testKthSmallest(self):
        self.assertEqual(kthSmallest(buildBinaryTree(
            [3, 1, 4, None, 2]), 1), 1)
        self.assertEqual(kthSmallest(buildBinaryTree(
            [5, 3, 6, 2, 4, None, None, 1]), 3), 3)

    def testIsValidBST(self):
        self.assertEqual(isValidBST(buildBinaryTree([2, 1, 3])), True)
        self.assertEqual(isValidBST(buildBinaryTree(
            [5, 1, 4, None, None, 3, 6])), False)

    def testPathSum(self):
        self.assertEqual(pathSum(buildBinaryTree(
            [5, 4, 8, 11, None, 13, 4, 7, 2, 5, 1]), 22), 3)


if __name__ == '__main__':
    unittest.main()
