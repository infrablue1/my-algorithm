"""
Leetcode link: https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.

example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

from .binary_tree_utils import TreeNode


def invertTree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return root
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
