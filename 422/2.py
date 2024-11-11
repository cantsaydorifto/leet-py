class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        dp = [[0] * len(moveTime[0]) for _ in range(len(moveTime))]
        for i in range(len(moveTime)):
            for j in range(len(moveTime[0])):
                if i == 0 and j == 0:
                    dp[i][j] = moveTime[i][j]
                    continue
                if i == 0:
                    dp[i][j] = (
                        moveTime[i][j] + 1
                        if dp[i][j - 1] <= moveTime[i][j]
                        else dp[i][j - 1] + 1
                    ) 
                    continue
                if j == 0:
                    dp[i][j] = (
                        moveTime[i][j] + 1
                        if dp[i - 1][j] <= moveTime[i][j]
                        else dp[i - 1][j] + 1
                    )
                    continue
                if min(dp[i - 1][j], dp[i][j - 1]) > moveTime[i][j]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = moveTime[i][j] + 1
        return dp[-1][-1]


print(Solution().minTimeToReach([[0, 4, 8], [10, 20, 15]]))
print(Solution().minTimeToReach(moveTime=[[0, 4], [4, 4]]))
print(Solution().minTimeToReach(moveTime=[[0, 0, 0], [0, 0, 0]]))
print(Solution().minTimeToReach(moveTime=[[0, 1], [1, 2]]))
print(Solution().minTimeToReach([[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]))
