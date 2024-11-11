class Solution:
    def lessThanEqualGoal(self, goal: int):
        res, l, d = 0, 0, {}
        if goal < 0:
            return 0
        for i in range(len(self.nums)):
            d[self.nums[i]] = d.get(self.nums[i], 0) + 1
            while len(d) > goal:
                d[self.nums[l]] = d.get(self.nums[l], 0) - 1
                if d[self.nums[l]] == 0:
                    d.pop(self.nums[l])
                l += 1
            res += i - l + 1
        return res

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        self.nums = nums
        return self.lessThanEqualGoal(k) - self.lessThanEqualGoal(k - 1)


print(Solution().subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
print(Solution().subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
