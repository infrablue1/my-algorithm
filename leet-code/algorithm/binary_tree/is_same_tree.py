"""
Leetcode link: https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they
are the same or not. Two binary trees are considered the same if they are
structurally identical, and the nodes have the same value.

example:
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

from .binary_tree_utils import TreeNode


def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and \
            isSameTree(p.right, q.right)
    return not p and not q
