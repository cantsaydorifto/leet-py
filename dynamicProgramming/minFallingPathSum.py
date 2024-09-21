class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1:
                    dp[i][j] = grid[i][j]
                    continue
                if j == 0:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
                    continue
                if j == len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j - 1], dp[i + 1][j])
                    continue
                dp[i][j] = grid[i][j] + min(
                    dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]
                )
        return min(dp[0])

    def getMinExceptOne(self, arr: list[int], idxToSkip: int):
        res = float("inf")
        for i in range(len(arr)):
            if i == idxToSkip:
                continue
            res = min(res, arr[i])
        return res

    def minFallingPathSum2(self, grid: list[list[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1:
                    dp[i][j] = grid[i][j]
                    continue
                dp[i][j] = grid[i][j] + self.getMinExceptOne(dp[i + 1], j)
        for i in dp:
            print(i)
        return min(dp[0])


# print(Solution().minFallingPathSum(grid=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
# print(Solution().minFallingPathSum(grid=[[-19, 57], [-40, -5]]))
print(Solution().minFallingPathSum2(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(Solution().minFallingPathSum2(grid=[[7]]))
