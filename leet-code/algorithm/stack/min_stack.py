"""
Leetcode link: https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.
Implement the MinStack class:
1. MinStack() initializes the stack object.
2. void push(int val) pushes the element val onto the stack.
3. void pop() removes the element on the top of the stack.
4. int top() gets the top element of the stack.
5. int getMin() retrieves the minimum element in the stack.
6. You must implement a solution with O(1) time complexity for each function.

example:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""


class MinStack:
    def __init__(self):
        self.data = []
        self.stk = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.stk) == 0:
            self.stk.append(val)
        else:
            self.stk.append(min(val, self.stk[-1]))

    def pop(self) -> None:
        self.stk.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.stk[-1]
