from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            elementsAtLevel = []
            qlenAtLevel = len(q)
            for _ in range(qlenAtLevel):
                t = q.popleft()
                elementsAtLevel.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(elementsAtLevel)
        return res
