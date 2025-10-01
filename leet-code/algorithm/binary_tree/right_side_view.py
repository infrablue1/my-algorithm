"""
Leetcode link: https://leetcode.com/problems/binary-tree-right-side-view/
Given the root of a binary tree, imagine yourself standing on the right side of
it, return the values of the nodes you can see ordered from top to bottom.

example:
Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]
"""

from .binary_tree_utils import TreeNode


def rightSideView(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    q = []
    ans = []
    q.append(root)
    while len(q) > 0:
        ans.append(q[0].val)
        tmp = []
        for node in q:
            if node.right:
                tmp.append(node.right)
            if node.left:
                tmp.append(node.left)
        q = tmp

    return ans
