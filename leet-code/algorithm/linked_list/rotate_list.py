"""
Leetcode link: https://leetcode.com/problems/rotate-list/
Given the head of a linked list, rotate the list to the right by k places.

example:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""

from .linked_list_utils import ListNode


def rotateRight(head: ListNode | None, k: int) -> ListNode | None:
    dummy = ListNode(0, head)
    prev = dummy
    list_length = 0
    while prev.next:
        prev = prev.next
        list_length += 1

    if list_length == 0:
        return head
    k %= list_length
    if k == 0:
        return head

    left_count = list_length - k
    tail = prev
    prev = dummy
    for _ in range(left_count):
        prev = prev.next

    new_head = prev.next
    prev.next = None
    tail.next = dummy.next
    dummy.next = new_head

    return dummy.next
