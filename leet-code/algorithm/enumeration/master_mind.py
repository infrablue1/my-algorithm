"""
Leetcode link: https://leetcode.cn/problems/master-mind-lcci/
The Game of Master Mind is played as follows:
The computer has four slots, and each slot will contain a ball that is red (R).
yellow (Y). green (G) or blue (B). For example, the computer might have RGGB
(Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess
YRGB. When you guess the correct color for the correct slot, you get a "hit:'
If you guess a color that exists but is in the wrong slot, you get a
"pseudo-hit:' Note that a slot that is a hit can never count as a pseudo-hit.
For example, if the actual solution is RGBY and you guess GGRR, you have one
hit and one pseudo-hit. Write a method that, given a guess and a solution,
returns the number of hits and pseudo-hits.
Given a sequence of colors solution, and a guess, write a method that return
the number of hits and pseudo-hit answer, where answer[0] is the number of hits
and answer[1] is the number of pseudo-hit.

example:
Input:  solution="RGBY",guess="GGRR"
Output:  [1,1]
Explanation:  hit once, pseudo-hit once.
"""


def masterMind(solution: str, guess: str) -> list[int]:
    n = len(solution)
    hit = 0
    solutionDict = {"R": 0, "Y": 0, "G": 0, "B": 0}
    guessDict = {"R": 0, "Y": 0, "G": 0, "B": 0}
    for i in range(n):
        if solution[i] == guess[i]:
            hit += 1
        else:
            solutionDict[solution[i]] += 1
            guessDict[guess[i]] += 1

    presudo_hit = 0
    for key in solutionDict:
        presudo_hit += min(solutionDict[key], guessDict[key])

    return [hit, presudo_hit]
