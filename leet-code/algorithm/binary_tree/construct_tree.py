"""
Leetcode link:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-
traversal/
Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same
tree, construct and return the binary tree.

example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

from .binary_tree_utils import TreeNode
from collections import deque


def buildTreeFromPreorderInorder(preorder: list[int], inorder: list[int])\
      -> TreeNode | None:
    preorder = deque(preorder)

    def build(preorder: deque[int], inorder: list[int]) -> TreeNode | None:
        if inorder:
            value = preorder.popleft()
            index = inorder.index(value)
            node = TreeNode(value)
            node.left = build(preorder, inorder[:index])
            node.right = build(preorder, inorder[index + 1:])
            return node
        return None

    return build(preorder, inorder)


"""
Leetcode link:
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-
traversal/
Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the same
tree, construct and return the binary tree.

example:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
"""


def buildTreeFromInorderPostOrder(inorder: list[int], postorder: list[int]) \
        -> TreeNode | None:
    if inorder:
        value = postorder.pop()
        index = inorder.index(value)
        node = TreeNode(value)
        node.right = buildTreeFromInorderPostOrder(inorder[index + 1:],
                                                   postorder)
        node.left = buildTreeFromInorderPostOrder(inorder[:index], postorder)
        return node
    return None
