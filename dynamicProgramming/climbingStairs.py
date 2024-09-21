class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = [-1] * (n + 1)
        self.memo[0], self.memo[1] = 1, 1
        return self.tabulate2Vars()

    def dfs(self, n: int):
        if self.memo[n] != -1:
            return self.memo[n]
        self.memo[n] = self.dfs(n - 1) + self.dfs(n - 2)
        return self.memo[n]

    def tabulate(self):
        n = len(self.memo)
        for i in range(2, n):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2]
        return self.memo[-1]

    def tabulate2Vars(self):
        n = len(self.memo)
        prev1, prev2 = 1, 1
        for _ in range(2, n):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2


print(Solution().climbStairs(n=2))
print(Solution().climbStairs(n=3))
