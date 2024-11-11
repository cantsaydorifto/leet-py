import math


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        res = math.gcd(*nums) * math.lcm(*nums)
        for i in range(len(nums)):
            res = max(
                res,
                math.gcd(*(nums[:i] + nums[i + 1 :]))
                * math.lcm(*(nums[:i] + nums[i + 1 :])),
            )
        return res


print(Solution().maxScore(nums=[1, 2, 3, 4, 5]))
