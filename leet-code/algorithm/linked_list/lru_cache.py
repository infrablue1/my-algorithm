"""
Leetcode link: https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache. Implement the LRUCache class:
1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
2. int get(int key) Return the value of the key if the key exists, otherwise
return -1.
3. void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

example:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
"""


class LRUCache:

    class ListNode:
        def __init__(self, key: int = 0, value: int = 0,
                     prev: 'LRUCache.ListNode' = None,
                     next: 'LRUCache.ListNode' = None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = LRUCache.ListNode()
        self.tail = LRUCache.ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}

    def appendTail(self, node: ListNode) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def removeNode(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def get(self, key: int) -> int:
        node: LRUCache.ListNode = self.key2node.get(key, None)
        if node:
            self.removeNode(node)
            self.appendTail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node: LRUCache.ListNode = self.key2node.get(key, None)
        if node:
            self.removeNode(node)
            self.appendTail(node)
            node.value = value
        else:
            node = LRUCache.ListNode(key, value)
            if self.count < self.capacity:
                self.count += 1
            else:
                removed_node = self.head.next
                self.removeNode(removed_node)
                del self.key2node[removed_node.key]

            self.appendTail(node)
            self.key2node[key] = node
