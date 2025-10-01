"""
Leetcode link:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree. According to the definition of LCA on Wikipedia: “The lowest
common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant
of itself).”

example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
"""

from .binary_tree_utils import TreeNode


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') \
        -> 'TreeNode':
    if not root or root.val == p.val or root.val == q.val:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left or right
