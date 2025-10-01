"""
Leetcode link: https://leetcode.com/problems/roman-to-integer/
There are n gas stations along a circular route, where the amount of gas at the
ith station is gas[i]. You have a car with an unlimited gas tank and it costs
cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction, otherwise
return -1. If there exists a solution, it is guaranteed to be unique.

example:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(s: str) -> int:
    sym2val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    value = sym2val[s[n-1]]
    prev_unit = value

    for i in range(n - 2, -1, -1):
        unit = sym2val[s[i]]
        if unit >= prev_unit:
            value += unit
            prev_unit = unit
        else:
            value -= unit

    return value


"""
Leetcode link: https://leetcode.com/problems/integer-to-roman/
Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Given an integer, convert it to a Roman numeral.

example:
Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal
places.
"""


def intToRoman(num: int) -> str:
    val2sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    ans = ""
    for val, sym in val2sym:
        if num == 0:
            break
        count = num // val
        ans += count * sym
        num -= count * val
    
    return ans
