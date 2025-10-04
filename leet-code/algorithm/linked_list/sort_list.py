"""
Leetcode link: https://leetcode.com/problems/sort-list/
Given the head of a linked list, return the list after sorting it in ascending
order.

example:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

from .linked_list_utils import ListNode


def sortList(head: ListNode | None) -> ListNode | None:
    def mergeSort(head: ListNode | None) -> ListNode | None:
        if not head or head.next is None:
            return head

        # Split to 2 lists.
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        # Call recursive mergeSort.
        l1 = mergeSort(head)
        l2 = mergeSort(slow)

        # Merge two sorted lists.
        dummy = ListNode(0)
        prev = dummy
        while l1 and l2:
            if l1.val <= l2. val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2

        return dummy.next

    return mergeSort(head)
