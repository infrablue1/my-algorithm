"""
Leetcode link: https://leetcode.com/problems/partition-list/
Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x. You should preserve
the original relative order of the nodes in each of the two partitions.

example:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""

from .linked_list_utils import ListNode


def partition(head: ListNode | None, x: int) -> ListNode | None:
    dummy = ListNode(0, head)
    large_dummy = ListNode(0)
    prev = dummy
    large_prev = large_dummy

    while prev.next:
        cur = prev.next
        if cur.val >= x:
            # Move cur to large list.
            prev.next = cur.next
            cur.next = None
            large_prev.next = cur
            large_prev = large_prev.next
        else:
            prev = prev.next

    # Connect large list to returned list.
    prev.next = large_dummy.next
    return dummy.next
