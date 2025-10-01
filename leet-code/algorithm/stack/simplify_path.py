"""
Leetcode link: https://leetcode.com/problems/simplify-path/
You are given an absolute path for a Unix-style file system, which always
begins with a slash '/'. Your task is to transform this absolute path into its
simplified canonical path.

The rules of a Unix-style file system are as follows:
1. A single period '.' represents the current directory.
2. A double period '..' represents the previous/parent directory.
3. Multiple consecutive slashes such as '//' and '///' are treated as a single
slash '/'.
4. Any sequence of periods that does not match the rules above should be
treated as a valid directory or file name. For example, '...' and '....' are
valid directory or file names.

The simplified canonical path should follow these rules:
1. The path must start with a single slash '/'.
2. Directories within the path must be separated by exactly one slash '/'.
3. The path must not end with a slash '/', unless it is the root directory.
4. The path must not have any single or double periods ('.' and '..') used to
denote current or parent directories.
Return the simplified canonical path.

example:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.
"""


def simplifyPath(path: str) -> str:
    stk = []
    names = path.split('/')

    for name in names:
        if name == '.' or name == '':
            continue

        if name == '..':
            if len(stk) > 0:
                stk.pop()
        else:
            stk.append(name)

    return '/' + '/'.join(stk)
