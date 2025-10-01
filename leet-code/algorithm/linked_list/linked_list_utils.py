
class ListNode:
    def __init__(self, x, next: 'ListNode'=None):
        self.val = x
        self.next = next

def buildLinkedList(values: list[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return head.next

def buildLinkedListWithCycle(values: list[int], pos: int) -> ListNode:
    head = ListNode(0)
    idx = 0
    target_node: ListNode = None
    cur = head
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
        if idx == pos:
            target_node = cur

        idx += 1

    cur.next = target_node
    return head.next

def linkedList2List(node :ListNode | None):
    vals = []
    cur = node
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def buildRandomList(input: list[list[int]]) -> Node | None:
    index2node = {}
    idx = 0
    dummy = Node(0)
    cur = dummy
    for lst in input:
        val = lst[0]
        new_node = Node(val)
        index2node[idx] = new_node
        idx += 1
        cur.next = new_node
        cur = cur.next

    cur = dummy.next
    for lst in input:
        random_idx = lst[1]
        if random_idx != None:
            cur.random = index2node[random_idx]
        cur = cur.next

    return dummy.next

def randomList2List(node: Node | None) -> list[list[int]]:
    node2index = {}
    cur = node
    idx = 0
    while cur:
        node2index[cur] = idx
        idx += 1
        cur = cur.next

    vals = []
    cur = node
    while cur:
        random_val = node2index[cur.random] if cur.random else None
        vals.append([cur.val, random_val])
        cur = cur.next

    return vals
