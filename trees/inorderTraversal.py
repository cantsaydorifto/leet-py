# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.res = []
        self.dfsInorder(root)
        return self.res

    def iterative(self, root: TreeNode | None):
        if not root:
            return
        st = []
        t = root
        while st or t:
            while t:
                st.append(t)
                t = t.left
            t = st.pop()
            self.res.append(t.val)
            t = t.right

    def dfsInorder(self, root: TreeNode | None):
        if not root:
            return
        self.dfsInorder(root.left)
        self.res.append(root.val)
        self.dfsInorder(root.right)
