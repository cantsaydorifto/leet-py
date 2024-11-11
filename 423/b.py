class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        l = 1
        r = len(nums)
        res = 1
        while l < r:
            mid = (l + r) // 2
            if self.hasIncreasingSubarrays(nums, mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid
        return res

    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        res = self.checkIncreasingSubarray(nums, k)
        print(res, k)
        for i in res:
            if i + 1 + k <= len(nums) and self.checkIncreasingSubarrayFromIndex(
                nums, k, i + 1
            ):
                return True
        return False

    def checkIncreasingSubarray(self, nums: list[int], k: int) -> bool:
        res = []
        j = 0
        while j + k <= len(nums):
            is_increasing = True
            for i in range(j, j + k - 1):
                if nums[i] >= nums[i + 1]:
                    is_increasing = False
                    break
            if is_increasing:
                res.append(j)
            j += 1
        return res

    def checkIncreasingSubarrayFromIndex(self, nums: list[int], k: int, i: int) -> bool:
        for j in range(i, i + k - 1):
            if nums[j] >= nums[j + 1]:
                return False
        return True


# print(Solution().maxIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
# print(Solution().maxIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
# print(Solution().maxIncreasingSubarrays(nums=[-15, 19]))
print(Solution().maxIncreasingSubarrays(nums=[5, 8, -2, -1]))
