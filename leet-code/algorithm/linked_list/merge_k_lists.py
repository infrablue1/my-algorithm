"""
Leetcode link: https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order. Merge all the linked-lists into one sorted linked-list and
return it.

example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

"""

from .linked_list_utils import ListNode
import heapq


class CompareNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other: 'CompareNode'):
        return self.node.val < other.node.val


def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    pq = []
    for head in lists:
        if head:
            heapq.heappush(pq, CompareNode(head))

    dummy = ListNode(0)
    cur = dummy
    while len(pq) > 0:
        node = heapq.heappop(pq).node
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(pq, CompareNode(node.next))

    return dummy.next
