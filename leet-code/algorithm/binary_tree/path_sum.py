"""
Leetcode link: https://leetcode.com/problems/path-sum/
Given the root of a binary tree and an integer targetSum, return true if the
tree has a root-to-leaf path such that adding up all the values along the
path equals targetSum.
A leaf is a node with no children.

example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""

from .binary_tree_utils import TreeNode


def hasPathSum(root: TreeNode | None, targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    targetSum -= root.val
    return hasPathSum(root.left, targetSum) or \
        hasPathSum(root.right, targetSum)
