"""
Leetcode link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

from .linked_list_utils import ListNode


def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    # One pass solution.
    dummy = ListNode(0, head)
    slow, fast = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next

    return dummy.next
