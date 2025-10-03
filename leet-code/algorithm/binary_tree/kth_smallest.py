"""
Leetcode link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

example:
Input: root = [3,1,4,null,2], k = 1
Output: 1
"""

from .binary_tree_utils import TreeNode


def kthSmallest(root: TreeNode | None, k: int) -> int:
    if not root:
        return 0

    # Use preorder traverse.
    node: TreeNode = root
    stk = []
    index = 1
    ans = 0

    while len(stk) > 0 or node:
        while node:
            stk.append(node)
            node = node.left

        if len(stk) > 0:
            node = stk.pop()
            if index == k:
                ans = node.val
                break
            node = node.right
            index += 1

    return ans
