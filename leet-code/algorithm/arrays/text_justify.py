"""
Leetcode link: https://leetcode.com/problems/text-justification/
Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right)
justified. You should pack your words in a greedy approach; that is, pack as
many words as you can in each line. Pad extra spaces ' ' when necessary so that
each line has exactly maxWidth characters. Extra spaces between words should be
distributed as evenly as possible. If the number of spaces on a line does not
divide evenly between words, the empty slots on the left will be assigned more
spaces than the slots on the right. For the last line of text, it should be
left-justified, and no extra space is inserted between words.
Note:
1. A word is defined as a character sequence consisting of non-space characters
only.
2. Each word's length is guaranteed to be greater than 0 and not exceed
maxWidth.
3. The input array words contains at least one word.

example:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."],
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


def fullJustify(words: list[str], maxWidth: int) -> list[str]:

    # Print a single line.
    def justifySingleLine(words: list[str]):
        ans = words[0]
        totalLength = sum(len(word) for word in words)
        spaceLength = maxWidth - totalLength
        expectSpaceCount = len(words) - 1
        # Only one word
        if expectSpaceCount == 0:
            return ans + spaceLength * ' '

        spaceUnit = spaceLength // expectSpaceCount
        residual = spaceLength % expectSpaceCount

        for i in range(1, len(words)):
            ans += ' ' * spaceUnit
            if residual > 0:
                ans += ' '
                residual -= 1
            ans += words[i]

        return ans

    n = len(words)
    beginIndex = 0
    lineLength = len(words[0])
    ans = []

    for endIndex in range(1, n):
        if lineLength <= maxWidth:
            lineLength += len(words[endIndex]) + 1
        if lineLength > maxWidth:
            ans.append(justifySingleLine(words[beginIndex:endIndex]))
            beginIndex = endIndex
            lineLength = len(words[beginIndex])

    if lineLength > 0:
        # Last line is different.
        finalLine = ' '.join(words[beginIndex:n])
        spaceCount = maxWidth - len(finalLine)
        finalLine += spaceCount * ' '
        ans.append(finalLine)

    return ans
