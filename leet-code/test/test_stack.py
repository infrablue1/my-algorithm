import os
import sys

import unittest

parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(parent_path)

from algorithm.stack import (
    isValid,
    simplifyPath,
    MinStack,
    evalRPN,
    calculate
)


class TestStack(unittest.TestCase):

    def testIsValid(self):
        self.assertEqual(isValid("()"), True)
        self.assertEqual(isValid("()[]{}"), True)
        self.assertEqual(isValid("(]"), False)
        self.assertEqual(isValid("([])"), True)
        self.assertEqual(isValid("([)]"), False)

    def testSimplifyPath(self):
        self.assertEqual(simplifyPath("/home/"), "/home")
        self.assertEqual(simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(simplifyPath("/home/user/Documents/../Pictures"),
                         "/home/user/Pictures")
        self.assertEqual(simplifyPath("/../"), "/")
        self.assertEqual(simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d")

    def _testMinStack(self, commands: list[str], args: list[int],
                      expect: list[int | str]):
        min_stk: MinStack = None
        result = []
        for command, arg in zip(commands, args):
            if command == "MinStack":
                min_stk = MinStack()
                result.append("null")
            elif command == "push":
                min_stk.push(arg[0])
                result.append("null")
            elif command == "getMin":
                result.append(min_stk.getMin())
            elif command == "pop":
                min_stk.pop()
                result.append("null")
            elif command == "top":
                result.append(min_stk.top())

        self.assertEqual(result, expect)

    def testMinStack(self):
        self._testMinStack(["MinStack", "push", "push", "push", "getMin",
                            "pop", "top", "getMin"],
                           [[], [-2], [0], [-3], [], [], [], []],
                           ["null", "null", "null", "null", -3, "null",
                            0, -2])

    def testEvalRPN(self):
        self.assertEqual(evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/",
                                  "*", "17", "+", "5", "+"]), 22)

    def testCalculate(self):
        self.assertEqual(calculate("1 + 1"), 2)
        self.assertEqual(calculate(" 2-1 + 2 "), 3)
        self.assertEqual(calculate("(1+(4+5+2)-3)+(6+8)"), 23)


if __name__ == '__main__':
    unittest.main()
