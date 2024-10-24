class Solution:
    # K flips allowed
    def longestOnes(self, nums: list[int], k: int) -> int:
        res, l, count, oneCount = 0, 0, [0, 0], 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            if nums[r] == 1:
                oneCount = max(oneCount, count[nums[r]])
            while r - l + 1 - oneCount > k:
                count[nums[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res

    # No Filp One
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxOnes = 0
        curOnes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curOnes = 0
                continue
            curOnes += 1
            maxOnes = max(maxOnes, curOnes)
        return maxOnes
