# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return (
            abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def getDepth(self, root: TreeNode | None):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))