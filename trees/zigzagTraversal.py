from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res, q = [], deque([root])
        if not root:
            return []
        reverseLevel = True
        while q:
            qLen = len(q)
            levelEl = []
            for _ in range(qLen):
                t = q.popleft()
                levelEl.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(levelEl if reverseLevel else levelEl[::-1])
            reverseLevel = not reverseLevel
        return res
