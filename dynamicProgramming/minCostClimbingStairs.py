class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        self.cost, self.memo = cost, [-1] * len(cost)
        self.memo[-1], self.memo[-2] = self.cost[-1], self.cost[-2]
        return self.tabulate2vars()

    def dfs(self, i: int):
        if i > len(self.cost) - 1:
            return 0
        if i == len(self.cost) - 1:
            return self.cost[-1]
        return self.cost[i] + min(self.dfs(i + 1), self.dfs(i + 2))

    def dfsMemo(self, i: int):
        if i > len(self.cost) - 1:
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        self.memo[i] = self.cost[i] + min(self.dfsMemo(i + 1), self.dfsMemo(i + 2))
        return self.memo[i]

    def tabulate(self):
        for i in range(len(self.memo) - 3, -1, -1):
            self.memo[i] = self.cost[i] + min(self.memo[i + 1], self.memo[i + 2])
        return min(self.memo[0], self.memo[1])

    def tabulate2vars(self):
        prev1, prev2 = self.cost[-2], self.cost[-1]
        for i in range(len(self.cost) - 3, -1, -1):
            prev1, prev2 = self.cost[i] + min(prev1, prev2), prev1
        return min(prev1, prev2)


print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))
print(Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
