"""
Leetcode link: https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in s. Specifically:
1. Each letter in pattern maps to exactly one unique word in s.
2. Each unique word in s maps to exactly one letter in pattern.
3. No two letters map to the same word, and no two words map to the same letter

example:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".
"""


def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False
    word2index = {}
    char2index = {}

    for i in range(len(words)):
        if words[i] not in word2index:
            word2index[words[i]] = i
        if pattern[i] not in char2index:
            char2index[pattern[i]] = i

        if word2index[words[i]] != char2index[pattern[i]]:
            return False

    return True
