class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            elementSum = nums[l] + nums[r]
            if elementSum > target:
                r -= 1
            elif elementSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return [0, 0]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[2, 3, 4], target=6))
print(Solution().twoSum(nums=[-1, 0], target=-1))
