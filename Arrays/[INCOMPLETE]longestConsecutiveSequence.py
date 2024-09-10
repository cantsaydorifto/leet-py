class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if i - 1 in numSet:
                continue
            cnt = 1
            while i + 1 in numSet:
                i += 1
                cnt += 1
            res = max(res, cnt)
        return res


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
