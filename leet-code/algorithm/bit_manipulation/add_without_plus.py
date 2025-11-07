"""
Leetcode link: https://leetcode.cn/problems/add-without-plus-lcci/
Write a function that adds two numbers. You should not use + or any arithmetic
operators.

example:
Input: a = 1, b = 1
Output: 2
"""

"""
C++ code:
int add(int a, int b) {
    while (b != 0) {
        unsigned int carry = (unsigned int) (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}
"""
