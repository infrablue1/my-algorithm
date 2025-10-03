"""
Leetcode link: https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take
course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.
Return true if you can finish all courses. Otherwise, return false.

example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
"""

from collections import defaultdict
from queue import Queue


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    indegrees = [0] * numCourses
    for prerequisite in prerequisites:
        cur, prev = prerequisite[0], prerequisite[1]
        graph[prev].append(cur)
        indegrees[cur] += 1

    q = Queue()
    for course in range(numCourses):
        if indegrees[course] == 0:
            q.put(course)

    count = 0
    while not q.empty():
        cur = q.get()
        count += 1
        for nextCourse in graph[cur]:
            indegrees[nextCourse] -= 1
            if indegrees[nextCourse] == 0:
                q.put(nextCourse)

    return count == numCourses


"""
Leetcode link: https://leetcode.com/problems/course-schedule-ii/
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take
course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.
Return the ordering of courses you should take to finish all courses. If there
are many valid answers, return any of them. If it is impossible to finish all
courses, return an empty array.

example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0, 1]
Explanation: There are a total of 2 courses to take. To take course 1 you
should have finished course 0. So the correct course order is [0,1].
"""


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    indegrees = [0] * numCourses
    for prerequisite in prerequisites:
        cur, prev = prerequisite[0], prerequisite[1]
        graph[prev].append(cur)
        indegrees[cur] += 1

    q = Queue()
    for course in range(numCourses):
        if indegrees[course] == 0:
            q.put(course)

    ans = []
    while not q.empty():
        cur = q.get()
        ans.append(cur)
        for nextCourse in graph[cur]:
            indegrees[nextCourse] -= 1
            if indegrees[nextCourse] == 0:
                q.put(nextCourse)

    return ans if len(ans) == numCourses else []
