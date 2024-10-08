# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.dfs(root)

    def dfs(self, root: TreeNode | None):
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
