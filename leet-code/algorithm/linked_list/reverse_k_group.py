"""
Leetcode link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Given the head of a linked list, reverse the nodes of the list k at a time, and
return the modified list. k is a positive integer and is less than or equal to
the length of the linked list. If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be
changed.

example:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""

from .linked_list_utils import ListNode


def reverseKGroup(head: ListNode | None, k: int) -> ListNode | None:
    dummy = ListNode(0, head)
    count = 0
    cur = head
    while cur:
        cur = cur.next
        count += 1

    prev = dummy
    for _ in range(count // k):
        cur = prev.next
        # Reverse each sub group.
        for _ in range(k - 1):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        # Move to next sub group.
        for _ in range(k):
            prev = prev.next

    return dummy.next
