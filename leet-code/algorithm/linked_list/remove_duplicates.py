"""
Leetcode link:
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list. Return the
linked list sorted as well.

example:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

from .linked_list_utils import ListNode


def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next:
        cur = prev.next
        count = 1
        val = cur.val
        while cur.next and cur.next.val == val:
            count += 1
            cur = cur.next

        if count > 1:
            prev.next = cur.next
        else:
            prev = prev.next

    return dummy.next
