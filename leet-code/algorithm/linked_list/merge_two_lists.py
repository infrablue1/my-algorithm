"""
Leetcode link: https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2. Merge the
two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.
Return the head of the merged linked list.

example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

from .linked_list_utils import ListNode

def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    l1, l2 = list1, list2

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 if l1 else l2
    return dummy.next
