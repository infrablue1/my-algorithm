"""
Leetcode link: https://leetcode.cn/problems/pattern-matching-lcci/
You are given two strings, pattern and value. The pattern string consists of
just the letters a and b, describing a pattern within a string. For example,
the string catcatgocatgo matches the pattern aabab (where cat is a and go is
b). It also matches patterns like a, ab, and b. Write a method to determine if
value matches pattern. a and b cannot be the same string.

example:
Input:  pattern = "abba", value = "dogcatcatdog"
Output:  true
"""


def patternMatching(pattern: str, value: str) -> bool:
    countA, countB = 0, 0
    for ch in pattern:
        if ch == 'a':
            countA += 1
        else:
            countB += 1

    # Pattern is empty then value must be empty.
    if len(pattern) == 0:
        return len(value) == 0
    # If value is empty, pattern cound be empty or only one letter.
    if len(value) == 0:
        return len(pattern) == 0 or (countA == 0 or countB == 0)

    # Now both pattern and value are not empty.
    # Ensure that countA >= countB
    if countA < countB:
        pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
        countA, countB = countB, countA

    length = len(value)
    for lenA in range(length // countA + 1):
        remain = length - lenA * countA
        if (countB == 0 and remain == 0) or \
           (countB != 0 and remain % countB == 0):
            lenB = 0 if countB == 0 else remain // countB
            pos, flag = 0, True
            subA, subB = None, None

            for ch in pattern:
                if ch == 'a':
                    sub = value[pos:pos+lenA]
                    if not subA:
                        subA = sub
                    elif sub != subA:
                        flag = False
                        break
                    pos += lenA
                else:
                    sub = value[pos:pos+lenB]
                    if not subB:
                        subB = sub
                    elif sub != subB:
                        flag = False
                        break
                    pos += lenB

            if flag and subA != subB:
                return True
    return False
