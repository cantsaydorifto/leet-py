class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        self.res = float("inf")
        self.grid = grid
        ch = 0  # 0 for optimized 1 for recursive
        if ch == 0:
            self.optimized()
        else:
            self.dfs(0, 0, 0)
        return self.res

    def optimized(self):
        grid = self.grid
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    dp[i][j] = grid[-1][-1]
                elif i == len(grid) - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
        self.res = dp[0][0]

    def dfs(self, i: int, j: int, pathSum: int):
        if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1:
            self.res = min(pathSum + self.grid[i][j], self.res)
            return
        if i > len(self.grid) - 1 or j > len(self.grid[0]) - 1:
            return
        self.dfs(i + 1, j, pathSum + self.grid[i][j])
        self.dfs(i, j + 1, pathSum + self.grid[i][j])


print(Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
print(
    Solution().minPathSum(
        grid=[
            [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
            [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
            [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
            [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
            [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
            [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
            [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
            [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
            [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
            [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
            [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
            [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9],
        ]
    )
)
