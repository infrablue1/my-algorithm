"""
Leetcode link: https://leetcode.cn/problems/paths-with-sum-lcci/
You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of
paths that sum to a given value. The path does not need to start or end at the
root or a leaf, but it must go downwards (traveling only from parent nodes to
child nodes).

example:
Given the following tree and  sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
Output:

3
Explanation: Paths that have sum 22 are: [5,4,11,2], [5,8,4,5], [4,11,7]
"""

from .binary_tree_utils import TreeNode


def pathSum(root: TreeNode | None, sum: int) -> int:
    prefixDict = {}

    def dfs(root: TreeNode | None, curSum: int) -> int:
        if not root:
            return 0
        curSum += root.val
        ret = 0
        if curSum - sum in prefixDict:
            ret = prefixDict[curSum - sum]

        prefixDict[curSum] = prefixDict.get(curSum, 0) + 1
        ret += dfs(root.left, curSum)
        ret += dfs(root.right, curSum)
        prefixDict[curSum] -= 1
        return ret

    prefixDict[0] = 1
    return dfs(root, 0)
