class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[0] * len(triangle[i]) for i in range(len(triangle))]

        for i in range(len(triangle) - 1, -1, -1):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if i == len(triangle) - 1:
                    dp[i][j] = triangle[i][j]
                    continue
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


print(Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minimumTotal([[-10]]))
