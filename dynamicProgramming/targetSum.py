class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.dp = {}
        self.table = []
        return self.dfs(0, nums[0]) + self.dfs(0, -nums[0])

    def dfs(self, i: int, res: int):
        if (i, res) in self.dp:
            return self.dp[(i, res)]
        if i == len(self.nums) - 1 and self.target == res:
            return 1
        if i == len(self.nums) - 1:
            return 0
        self.dp[(i, res)] = self.dfs(i + 1, res + self.nums[i + 1]) + self.dfs(
            i + 1, res - self.nums[i + 1]
        )
        return self.dp[(i, res)]


print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
print(
    Solution().findTargetSumWays(
        nums=[
            18,
            50,
            26,
            2,
            15,
            14,
            14,
            2,
            42,
            43,
            38,
            44,
            24,
            17,
            19,
            25,
            3,
            10,
            42,
            20,
        ],
        target=24,
    )
)
