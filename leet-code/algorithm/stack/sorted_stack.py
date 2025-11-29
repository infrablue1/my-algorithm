"""
Leetcode link: https://leetcode.cn/problems/sort-of-stacks-lcci/
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure (such as an array). The stack supports the
following operations: push, pop, peek, and isEmpty. When the stack is empty,
peek should return -1.

example:
Input:
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
Output:
[null,null,null,1,null,2]
"""


class SortedStack:

    def __init__(self):
        self.data = []
        self.tmp = []

    def push(self, val: int) -> None:
        maxValue = 5001 if len(self.data) == 0 else self.data[-1]
        minValue = -5001 if len(self.tmp) == 0 else self.tmp[-1]
        while True:
            if val > maxValue:
                self.tmp.append(self.data.pop())
                maxValue = 5001 if len(self.data) == 0 else self.data[-1]
            elif val < minValue:
                self.data.append(self.tmp.pop())
                minValue = -5001 if len(self.tmp) == 0 else self.tmp[-1]
            else:
                self.data.append(val)
                break

    def pop(self) -> None:
        while len(self.tmp) > 0:
            self.data.append(self.tmp.pop())
        if len(self.data) > 0:
            self.data.pop()

    def peek(self) -> int:
        while len(self.tmp) > 0:
            self.data.append(self.tmp.pop())
        return self.data[-1] if len(self.data) > 0 else -1

    def isEmpty(self) -> bool:
        return len(self.data) == 0 and len(self.tmp) == 0
