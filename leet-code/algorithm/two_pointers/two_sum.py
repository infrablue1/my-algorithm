"""
Leetcode link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length. Return the indices of the two
numbers, index1 and index2, added by one as an integer array [index1, index2]
of length 2.
The tests are generated such that there is exactly one solution. You may not
use the same element twice. Your solution must use only constant extra space.

example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
We return [1, 2].
"""


def twoSum2(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    i, j = 0, n - 1

    while i < j:
        a = target - numbers[i]
        while i < j and numbers[j] > a:
            j -= 1
        if numbers[j] == a:
            break
        i += 1

    return [i + 1, j + 1]
