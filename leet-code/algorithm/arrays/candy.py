"""
Leetcode link: https://leetcode.com/problems/candy/
There are n children standing in a line. Each child is assigned a rating value
given in the integer array ratings. You are giving candies to these children
subjected to the following requirements:
1. Each child must have at least one candy.
2 .Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies
to the children.

example:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2
candies respectively.
"""


def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i + 1] + 1, candies[i])

    return sum(candies)
