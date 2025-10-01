"""
Leetcode link: https://leetcode.com/problems/symmetric-tree/
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

example:
Input: root = [1,2,2,3,4,4,3]
Output: true
"""

from .binary_tree_utils import TreeNode


def isSymmetric(root: TreeNode | None) -> bool:
    def isSame(r1: TreeNode | None, r2: TreeNode | None) -> bool:
        if not r1 and not r2:
            return True
        if r1 and r2:
            return r1.val == r2.val and isSame(r1.left, r2.right) and \
                isSame(r1.right, r2.left)
        return False
    return isSame(root, root)
