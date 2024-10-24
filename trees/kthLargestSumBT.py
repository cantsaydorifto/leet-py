# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        import heapq
        from collections import deque

        levelSums = []
        q = deque([root])
        while q and root:
            qLen = len(q)
            curLevelSum = 0
            for _ in range(qLen):
                t = q.pop()
                curLevelSum += t.val
                if t.left:
                    q.appendleft(t.left)
                if t.right:
                    q.appendleft(t.right)
            heapq.heappush(levelSums, -curLevelSum)
        if k > len(levelSums):
            return -1
        while k > 1:
            heapq.heappop(levelSums)
            k -= 1
        return -heapq.heappop(levelSums)
