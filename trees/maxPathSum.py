# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        self.dfs(root)
        return self.res

    def dfs(self, root: TreeNode | None):
        if not root:
            return 0
        leftSum = max(self.dfs(root.left), 0)
        rightSum = max(self.dfs(root.right), 0)
        self.res = max(self.res, root.val + leftSum + rightSum)
        return root.val + max(leftSum, rightSum)
