"""
Leetcode link:
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
You are given a string s and an array of strings words. All the strings of
words are of the same length. A concatenated string is a string that exactly
contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
"cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not
a concatenated string because it is not the concatenation of any permutation of
words.
Return an array of the starting indices of all the concatenated substrings in
s. You can return the answer in any order.

example:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of
["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of
["foo","bar"] which is a permutation of words.
"""


def findSubstring(s: str, words: list[str]) -> list[int]:
    numWords = len(words)
    n = len(s)
    wordLen = len(words[0])
    wordCountDict = {}
    for word in words:
        wordCountDict[word] = wordCountDict.get(word, 0) + 1

    ans = []
    for i in range(wordLen):
        seen = {}
        size = 0
        j = i

        while j + wordLen < n:
            sub = s[j:j + wordLen]
            if sub not in wordCountDict:
                size = 0
                seen.clear()
                j += wordLen
                continue

            size += 1
            seen[sub] = seen.get(sub, 0) + 1

            while seen[sub] > wordCountDict[sub]:
                start = j - (size - 1) * wordLen
                tmp = s[start:start + wordLen]
                seen[tmp] -= 1
                size -= 1

            if size == numWords:
                ans.append(j - (size - 1) * wordLen)

            j += wordLen

    return ans
