"""
Leetcode link:
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

example:
Input: root = [4,2,6,1,3]
Output: 1
"""

from .binary_tree_utils import TreeNode


def getMinimumDifference(root: TreeNode | None) -> int:
    if not root:
        return 0

    # Use preorder traverse.
    node: TreeNode = root
    stk = []
    ans = 1e5 + 1
    prev = -1e5 - 1

    while len(stk) > 0 or node:
        while node:
            stk.append(node)
            node = node.left

        if len(stk) > 0:
            node = stk.pop()
            ans = min(ans, node.val - prev)
            prev = node.val
            node = node.right

    return ans
