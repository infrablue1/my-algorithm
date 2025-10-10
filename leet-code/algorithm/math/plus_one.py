"""
Leetcode link: https://leetcode.com/problems/plus-one/
You are given a large integer represented as an integer array digits, where
each digits[i] is the ith digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large
integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

example:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""


def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)
    ans = digits.copy()
    i = n - 1

    while i >= 0:
        if ans[i] + 1 < 10:
            ans[i] = ans[i] + 1
            return ans

        ans[i] = 0
        i -= 1

    if i < 0:
        ans.insert(0, 1)

    return ans
