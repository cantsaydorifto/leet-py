class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums) - k + 1):
            if self.checkIncreasingSubarray(
                nums, k, i
            ) and self.checkIncreasingSubarray(nums, k, i + k):
                return True
        return False

    def checkIncreasingSubarray(self, nums: list[int], k: int, i: int) -> bool:
        ki = k
        l = i
        while ki > 1 and l < len(nums) - 1:
            if nums[l] >= nums[l + 1]:
                return False
            ki -= 1
            l += 1
        return True if ki == 1 else False


print(Solution().hasIncreasingSubarrays([7, -1, -99, 1, 2, 3, 4, 5, 6], 3))  # True
# print(Solution().checkIncreasingSubarray([1, 2, 3, 4, 5], 4))  # True
# print(Solution().checkIncreasingSubarray([1, 2, 3, 4, 5], 5))  # True
