class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res, l, t, oddCnt = 0, 0, 0, 0
        for i in nums:
            if i % 2 != 0:
                oddCnt += 1
            while oddCnt > k:
                if nums[t] % 2 != 0:
                    oddCnt -= 1
                t += 1
                l = t
            if oddCnt == k:
                while nums[t] % 2 == 0:
                    t += 1
                res += t - l + 1
        return res


print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(Solution().numberOfSubarrays(nums=[2, 4, 6], k=1))
print(Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
