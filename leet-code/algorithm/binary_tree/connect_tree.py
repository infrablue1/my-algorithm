"""
Leetcode link:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

example:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
"""

from .binary_tree_utils import TreeNode


def connect(root: TreeNode) -> TreeNode:
    node = root
    while node:
        dummy = TreeNode()
        cur = dummy
        while node:
            if node.left:
                cur.next = node.left
                cur = cur.next
            if node.right:
                cur.next = node.right
                cur = cur.next
            node = node.next
        # Move to next level.
        node = dummy.next
    return root
