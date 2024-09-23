class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.res: list[int] = []
        self.dfs(root)
        return self.res

    def iterative(self, root: TreeNode | None):
        st = []
        t = root
        while st or t:
            while t:
                st.append(t)
                self.res.append(t.val)
                t = t.left
            t = st.pop()
            t = t.right

    def usingStack(self, root: TreeNode | None):
        if not root:
            return []
        st = [root]
        while st:
            t = st.pop()
            self.res.append(t.val)
            if t.right:
                st.append(t.right)
            if t.left:
                st.append(t.left)

    def dfs(self, root: TreeNode | None):
        if not root:
            return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
