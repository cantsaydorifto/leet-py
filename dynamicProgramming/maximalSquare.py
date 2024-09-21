class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        maxResSquareLen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i == 0 or j == 0) and matrix[i][j] == "1":
                    dp[i][j] = 1
                    maxResSquareLen = max(maxResSquareLen, 1)
                    continue
                if (
                    matrix[i][j] == "1"
                    and dp[i - 1][j] != 0
                    and dp[i][j - 1] != 0
                    and dp[i - 1][j - 1] != 0
                ):
                    maxSquareLen = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    maxResSquareLen = max(maxResSquareLen, maxSquareLen)
                    dp[i][j] = maxSquareLen
                elif matrix[i][j] == "1":
                    dp[i][j] = 1
                    maxResSquareLen = max(maxResSquareLen, 1)
        # for i in dp:
        #     print(i)
        return maxResSquareLen * maxResSquareLen


print(
    Solution().maximalSquare(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
        ]
    )
)
print(Solution().maximalSquare([["1", "1", "1", "1"], ["1", "1", "1", "1"]]))
print(
    Solution().maximalSquare(
        matrix=[
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
print(Solution().maximalSquare([["0", "1"], ["1", "0"]]))
