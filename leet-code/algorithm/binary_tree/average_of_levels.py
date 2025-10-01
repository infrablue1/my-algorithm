"""
Leetcode link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given the root of a binary tree, return the average value of the nodes on each
level in the form of an array. Answers within 10-5 of the actual answer will be
accepted.

example:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
and on level 2 is 11.
Hence return [3, 14.5, 11].
"""

from .binary_tree_utils import TreeNode
from queue import Queue


def averageOfLevels(root: TreeNode | None) -> list[float]:
    if not root:
        return []

    q = Queue()
    ans = []
    q.put(root)

    while not q.empty():
        total = 0
        qsize = q.qsize()
        for _ in range(qsize):
            node: TreeNode = q.get()
            total += node.val
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        ans.append(total / qsize)

    return ans
