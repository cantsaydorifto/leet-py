class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        frontPro, backPro = 1, 1
        for i in range(1, len(res)):
            frontPro *= nums[i - 1]
            res[i] *= frontPro
        for i in range(len(res) - 2, -1, -1):
            backPro *= nums[i + 1]
            res[i] *= backPro
        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
# [1, 1, 2, 6]
# [24, 12, 4, 1]
