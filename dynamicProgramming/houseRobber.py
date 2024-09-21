class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1, prev2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev1, prev2 = prev2, max(nums[i] + prev1, prev2)
        return prev2

    # cirular - house robber 2
    def rob2(self, nums: list[int]) -> int:
        return max(self.rob(nums[:-1]), self.rob(nums[1:]))

    def robMem(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])] + [-1] * (len(nums) - 2)
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]

    def dfs(self, i: int):
        return self.nums[i]

    def robN2(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        for i in range(len(nums) - 3, -1, -1):
            nums[i] += max(nums[i + 2 :])
        return max(nums[0], nums[1])


print(Solution().rob(nums=[1]))
print(Solution().rob(nums=[1, 2, 3, 1]))
print(Solution().rob(nums=[2, 7, 9, 3, 1]))
print(Solution().rob(nums=[1, 3, 1]))
print(Solution().rob(nums=[2, 1, 1, 2]))
