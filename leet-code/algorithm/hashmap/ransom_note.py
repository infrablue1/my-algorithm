"""
Leetcode link: https://leetcode.com/problems/ransom-note/
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

example:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_dict = {}
    for c in ransomNote:
        ransom_dict[c] = ransom_dict.get(c, 0) + 1

    magazine_dict = {}
    for c in magazine:
        magazine_dict[c] = magazine_dict.get(c, 0) + 1

    return all(ransom_dict[c] <= magazine_dict.get(c, 0) for c in ransom_dict)
