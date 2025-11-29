"""
Leetcode link: https://leetcode.cn/problems/closed-number-lcci/
Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation.

example:
Input: num = 2 (0b10)
Output: [4, 1] ([0b100, 0b1])
"""


def findClosedNumbers(num: int) -> list[int]:
    s = str(bin(num)[2:])
    bigstr = [ch for ch in s]
    if len(bigstr) < 31:
        bigstr = ['0'] + bigstr
    smallstr = [ch for ch in s]

    small = -1
    n = len(smallstr)
    # Convert first 10 to 01 and move all bits higher

    for i in range(n - 1, 0, -1):
        if smallstr[i-1] == '1' and smallstr[i] == '0':
            smallstr[i-1] = '0'
            smallstr[i] = '1'
            left, right = i + 1, n - 1
            while left < right:
                while left < right and smallstr[left] == '1':
                    left += 1
                while left < right and smallstr[right] == '0':
                    right -= 1
                smallstr[left], smallstr[right] = \
                    smallstr[right], smallstr[left]
            small = int(''.join(smallstr), 2)
            break

    # Convert first 01 to 10 and move all bits lower
    big = -1
    n = len(bigstr)
    for i in range(n - 1, 0, -1):
        if bigstr[i-1] == '0' and bigstr[i] == '1':
            bigstr[i-1], bigstr[i] = '1', '0'
            left, right = i + 1, n - 1
            while left < right:
                while left < right and bigstr[left] == '0':
                    left += 1
                while left < right and bigstr[right] == '1':
                    right -= 1
                bigstr[left], bigstr[right] = bigstr[right], bigstr[left]
            big = int(''.join(bigstr), 2)
            break
    return [big, small]
