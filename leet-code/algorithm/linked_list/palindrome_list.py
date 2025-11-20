"""
Leetcode link: https://leetcode.cn/problems/palindrome-linked-list-lcci/
Implement a function to check if a linked list is a palindrome.
Could you do it in O(n) time and O(1) space?

example:
Input:  1->2->2->1
Output:  true
"""

from .linked_list_utils import ListNode


def reverseList(head: ListNode | None) -> ListNode | None:
    if not head:
        return head
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


def isPalindrome(head: ListNode | None) -> bool:
    count = 0
    slow = head
    while slow:
        slow = slow.next
        count += 1

    if count <= 1:
        return True

    dummy = ListNode(0, head)
    slow, fast = dummy, dummy
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    midPrev = slow
    midHead = slow.next
    midPrev.next = None

    firstHead = head
    secondHead = reverseList(midHead)
    cur1, cur2 = firstHead, secondHead
    flag = True
    for _ in range(count // 2):
        if cur1.val != cur2.val:
            flag = False
            break
        cur1 = cur1.next
        cur2 = cur2.next

    midHead = reverseList(secondHead)
    midPrev = midHead
    return flag
