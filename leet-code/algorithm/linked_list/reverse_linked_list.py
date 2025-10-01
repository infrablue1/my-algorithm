"""
Leetcode link: https://leetcode.com/problems/reverse-linked-list-ii/
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

example:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""

from .linked_list_utils import ListNode


def reverseBetween(head: ListNode | None, left: int, right: int)\
      -> ListNode | None:
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    cur = prev.next
    for _ in range(right - left):
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = prev.next
        prev.next = tmp

    return dummy.next
