class Solution:
    def lessThanEqualGoal(self, goal: int):
        res, l, sum = 0, 0, 0
        if goal < 0:
            return 0
        for i in range(len(self.nums)):
            sum += self.nums[i]
            while sum > goal:
                sum -= self.nums[l]
                l += 1
            res += i - l + 1
        return res

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        self.nums = nums
        return self.lessThanEqualGoal(goal) - self.lessThanEqualGoal(goal - 1)


print(Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
print(Solution().numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
