class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i in range(len(nums)):
            if target - nums[i] in mp:
                return [mp[target - nums[i]], i]
            mp[nums[i]] = i
