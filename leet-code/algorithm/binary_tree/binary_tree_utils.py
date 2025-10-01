from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def buildBinaryTree(values: list[int | None]) -> TreeNode | None:
    n = len(values)
    if n == 0:
        return None

    root = TreeNode(values[0])
    q = Queue()
    q.put(root)
    i = 1

    while i < n:
        node: TreeNode = q.get()
        if not node:
            i += 1
            continue
        node.left = TreeNode(values[i]) if values[i] is not None else None
        i += 1
        if i < n:
            node.right = TreeNode(values[i]) if values[i] is not None else None
            i += 1
        q.put(node.left)
        q.put(node.right)

    return root


def binaryTree2List(root: TreeNode | None) -> list[int | None]:
    values = []
    if not root:
        return values

    q = Queue()
    q.put(root)
    while not q.empty():
        node: TreeNode | None = q.get()
        values.append(node.val if node else None)
        if node:
            q.put(node.left)
            q.put(node.right)

    # Rmove trailing None
    idx = len(values) - 1
    while idx >= 0:
        if values[idx] is not None:
            break
        idx -= 1

    return values[:idx + 1]


def findNode(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root:
        return None

    q = Queue()
    q.put(root)
    while not q.empty():
        node: TreeNode = q.get()
        if node.val == val:
            return node
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    return None


def binaryTree2ListWithNext(root: TreeNode | None) -> list[int | str]:
    if not root:
        return []

    node = root
    values = []
    q = Queue()
    q.put(root)
    while not q.empty():
        node: TreeNode = q.get()
        while not q.empty():
            q.get()

        cur = node
        while cur:
            values.append(cur.val)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
            cur = cur.next
        values.append("#")

    return values
