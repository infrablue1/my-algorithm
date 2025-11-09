"""
Leetcode link: https://leetcode.cn/problems/baby-names-lcci/
Each year, the government releases a list of the 10000 most common baby names
and their frequencies (the number of babies with that name). The only problem
with this is that some names have multiple spellings. For example,"John" and
''Jon" are essentially the same name but would be listed separately in the
list. Given two lists, one of names/frequencies and the other of pairs of
equivalent names, write an algorithm to print a new list of the true frequency
of each name. Note that if John and Jon are synonyms, and Jon and Johnny are
synonyms, then John and Johnny are synonyms. (It is both transitive and
symmetric.) In the final list, choose the name that are lexicographically
smallest as the "real" name.

example:
Input: names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"],
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
Output: ["John(27)","Chris(36)"]
"""


def trulyMostPopular(names: list[str], synonyms: list[str]) -> list[str]:
    countDict = {}
    unionMap = {}
    for name in names:
        i, j = name.find('('), name.find(')')
        count = int(name[i+1:j])
        realName = name[:i]
        countDict[realName] = count

    for synonym in synonyms:
        tmp = synonym.strip('()').split(',')
        n1, n2 = tmp[0], tmp[1]
        while n1 in unionMap:
            n1 = unionMap[n1]
        while n2 in unionMap:
            n2 = unionMap[n2]

        if n1 != n2:
            count = countDict.get(n1, 0) + countDict.get(n2, 0)
            smallName, bigName = n1, n2
            if n1 > n2:
                smallName, bigName = n2, n1
            unionMap[bigName] = smallName
            countDict.pop(bigName, None)
            countDict[smallName] = count

    ans = []
    for name in countDict:
        tmp = f"{name}({countDict[name]})"
        ans.append(tmp)

    return ans
