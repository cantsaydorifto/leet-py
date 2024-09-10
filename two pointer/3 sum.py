class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        nums.sort()
        # print(nums)
        self.res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(i + 1, len(nums) - 1)
        return self.res

    def twoSum(self, l: int, r: int) -> list[int]:
        i = l - 1
        while l < r:
            elementSum = self.nums[i] + self.nums[l] + self.nums[r]
            if elementSum > 0:
                r -= 1
            elif elementSum < 0:
                l += 1
            else:
                self.res.append([self.nums[i], self.nums[l], self.nums[r]])
                r -= 1
                while self.nums[r] == self.nums[r + 1] and l < r:
                    r -= 1
                l += 1
                while self.nums[l] == self.nums[l - 1] and l < r:
                    l += 1


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum(nums=[0, 1, 1]))
print(Solution().threeSum(nums=[0, 0, 0]))
