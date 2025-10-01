"""
Leetcode link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth. A binary tree's
maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

example:
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""

from .binary_tree_utils import TreeNode


def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
