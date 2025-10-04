"""
Leetcode link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order
and an integer k. Define a pair (u, v) which consists of one element from the
first array and one element from the second array. Return the k pairs (u1, v1),
(u2, v2), ..., (uk, vk) with the smallest sums.

example:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""

import heapq


class Pair:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b

    def __lt__(self, other: 'Pair') -> bool:
        return self.sum >= other.sum


def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) \
        -> list[list[int]]:
    m, n = len(nums1), len(nums2)
    pq = []

    for i in range(m):
        for j in range(n):
            pair = Pair(nums1[i], nums2[j])
            if len(pq) < k:
                # Push pair to heap directly.
                heapq.heappush(pq, pair)
            elif pair.sum < pq[0].sum:
                # Now the new pair cound be pushed to heap, remove the smallest
                # pair and push a new one.
                heapq.heappop(pq)
                heapq.heappush(pq, pair)
            else:
                break

    ans = [[pair.a, pair.b] for pair in pq]
    ans.sort(key=lambda x: (x[0], x[1]))
    return ans
