"""
Leetcode link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them. A node can only appear in
the sequence at most once. Note that the path does not need to pass through the
root. The path sum of a path is the sum of the node's values in the path. Given
the root of a binary tree, return the maximum path sum of any non-empty path.

example:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
= 42.
"""

from .binary_tree_utils import TreeNode


def maxPathSum(root: TreeNode | None) -> int:
    if not root:
        return 0

    ans = -1001

    def pathSum(root: TreeNode | None) -> int:
        if not root:
            return 0
        left = max(pathSum(root.left), 0)
        right = max(pathSum(root.right), 0)
        nonlocal ans
        ans = max(ans, root.val + left + right)
        return root.val + max(left, right)

    pathSum(root)
    return ans
