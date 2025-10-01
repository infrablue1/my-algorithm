"""
Leetcode link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).

example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""

from .binary_tree_utils import TreeNode
from queue import Queue


def levelOrder(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    q = Queue()
    ans = []
    q.put(root)

    while not q.empty():
        tmp = []
        qsize = q.qsize()
        for _ in range(qsize):
            node: TreeNode = q.get()
            tmp.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        ans.append(tmp)

    return ans
