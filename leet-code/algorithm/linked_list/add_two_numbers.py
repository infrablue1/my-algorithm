"""
Leetcode link: https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list. You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

from .linked_list_utils import ListNode


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    a, b = l1, l2

    while a or b or carry:
        val1 = a.val if a else 0
        val2 = b.val if b else 0

        a = a.next if a else a
        b = b.next if b else b

        total = val1 + val2 + carry
        carry = total // 10
        total %= 10
        cur.next = ListNode(total)
        cur = cur.next

    return dummy.next
