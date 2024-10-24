# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        depth = []
        from collections import deque

        q: deque[TreeNode | None] = deque([root])
        while q:
            levelSum = 0
            qLen = len(q)
            for _ in range(qLen):
                t = q.popleft()
                levelSum += t.val
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            depth.append(levelSum)

        q = deque([(root, 0)])
        while q:
            qLen = len(q)
            for _ in range(qLen):
                t, curDepth = q.popleft()
                print(t.val, curDepth)
                t.val = depth[curDepth] - t.val
                if t.left and t.right:
                    t.left.val, t.right.val = (
                        t.left.val + t.right.val,
                        t.left.val + t.right.val,
                    )
                if t.left:
                    q.append((t.left, curDepth + 1))
                if t.right:
                    q.append((t.right, curDepth + 1))
        return root

    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        self.d, self.depth, self.x, self.y = {}, {}, x, y
        self.dfs(root, None, 0)
        return self.depth[x] == self.depth[y] and self.d[x] != self.d[y]

    def dfs(self, root: TreeNode | None, parent: TreeNode | None, depth):
        if not root:
            return
        if root.val in [self.x, self.y]:
            self.d[root.val] = -1 if not parent else parent.val
            self.depth[root.val] = depth
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.left.left, root.left.right = TreeNode(4), TreeNode(6)
print(Solution().replaceValueInTree(root))
