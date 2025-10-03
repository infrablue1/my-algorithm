"""
Leetcode link: https://leetcode.com/problems/evaluate-division/
You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation
Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single
variable. You are also given some queries, where queries[j] = [Cj, Dj]
represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

example:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
"""

from collections import defaultdict
from queue import Queue


def calcEquation(equations: list[list[str]], values: list[float],
                 queries: list[list[str]]) -> list[float]:
    # Creat graph.
    graph = defaultdict(dict)
    for equation, value in zip(equations, values):
        x, y = equation[0], equation[1]
        graph[x][y] = value
        graph[y][x] = 1 / value

    # Query method for value of source -> dest.
    def getQuery(source: int, dest: int):
        q = Queue()
        q.put((source, 1.0))
        vis = set()

        while not q.empty():
            x, value = q.get()
            if x == dest:
                return value
            vis.add(x)

            for neighbor in graph[x]:
                if neighbor not in vis:
                    q.put((neighbor, value * graph[x][neighbor]))

        return - 1.0

    # Call getQuery for each pair.
    ans = []
    for query in queries:
        x, y = query[0], query[1]
        if x not in graph or y not in graph:
            ans.append(-1.0)
        else:
            ans.append(getQuery(x, y))

    return ans
