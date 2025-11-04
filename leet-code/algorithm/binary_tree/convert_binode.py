"""
Leetcode link: https://leetcode.cn/problems/binode-lcci/
The data structure TreeNode is used for binary tree, but it can also used to
represent a single linked list (where left is null, and right is the next
node in the list). Implement a method to convert a binary search tree
(implemented with TreeNode) into a single linked list. The values should be
kept in order and the operation should be performed in place (that is, on
the original data structure).
Return the head node of the linked list after converting.

example:
Input:  [4,2,5,1,3,null,6,0]
Output:  [0,null,1,null,2,null,3,null,4,null,5,null,6]
"""

from .binary_tree_utils import TreeNode


def convertBiNode(root: TreeNode | None) -> TreeNode | None:
    head = TreeNode(0)
    prev = head

    def flat(root: TreeNode | None) -> None:
        if not root:
            return
        nonlocal prev
        flat(root.left)
        prev.right = root
        prev = root
        root.left = None
        flat(root.right)

    flat(root)
    return head.right
