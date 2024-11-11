class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res, l, sum = float("inf"), 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                res = min(res, i - l + 1)
                sum -= nums[l]
                l += 1
        return 0 if res == float("inf") else res


# print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
# print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))
# print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
# print(Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))
print(Solution().minSubArrayLen(target=3, nums=[2, -1, 2]))
