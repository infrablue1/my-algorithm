"""
Leetcode link: https://leetcode.cn/problems/check-subtree-lcci/
T1 and T2 are two very large binary trees. Create an algorithm to determine if
T2 is a subtree of T1. A tree T2 is a subtree of T1 if there exists a node n
in T1 such that the subtree of n is identical to T2. That is, if you cut off
the tree at node n, the two trees would be identical.

example:
Input: t1 = [1, 2, 3], t2 = [2]
Output: true
"""

from .binary_tree_utils import TreeNode


def checkSubTree(t1: TreeNode | None, t2: TreeNode | None) -> bool:
    subDepth = -1
    hasSubtree = False

    def equal(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and equal(t1.left, t2.left) and \
            equal(t1.right, t2.right)

    def maxDepth(node: TreeNode | None, t2: TreeNode | None) -> int:
        nonlocal hasSubtree
        if hasSubtree is True or node is None:
            return 0
        depth = max(maxDepth(node.left, t2), maxDepth(node.right, t2)) + 1
        hasSubtree |= depth == subDepth and equal(node, t2)
        return depth

    subDepth = maxDepth(t2, t2)
    maxDepth(t1, t2)
    return hasSubtree
