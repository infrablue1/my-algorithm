"""
Leetcode link: https://leetcode.com/problems/count-complete-tree-nodes/
Given the root of a complete binary tree, return the number of the nodes in the
tree. According to Wikipedia, every level, except possibly the last, is
completely filled in a complete binary tree, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at
the last level h.
Design an algorithm that runs in less than O(n) time complexity.

example:
Input: root = [1,2,3,4,5,6]
Output: 6
"""

from .binary_tree_utils import TreeNode


def countNodes(root: TreeNode | None) -> int:
    left_height, right_height = 0, 0
    node = root
    while node:
        left_height += 1
        node = node.left

    node = root
    while node:
        right_height += 1
        node = node.right

    if left_height == right_height:
        return 2 ** left_height - 1

    return 1 + countNodes(root.left) + countNodes(root.right)
