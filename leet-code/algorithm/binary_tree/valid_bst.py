"""
Leetcode link: https://leetcode.com/problems/validate-binary-search-tree/
Given the root of a binary tree, determine if it is a valid binary search tree.
A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys strictly less than
the node's key.
2. The right subtree of a node contains only nodes with keys strictly greater
than the node's key.
3. Both the left and right subtrees must also be binary search trees.

example:
Input: root = [2,1,3]
Output: true
"""

from .binary_tree_utils import TreeNode
from math import inf


def isValidBST(root: TreeNode | None) -> bool:
    # Use preorder traverse.
    node: TreeNode = root
    stk = []
    prev = float(-inf)

    while len(stk) > 0 or node:
        while node:
            stk.append(node)
            node = node.left

        if len(stk) > 0:
            node = stk.pop()
            if node.val <= prev:
                return False
            prev = node.val
            node = node.right

    return True
