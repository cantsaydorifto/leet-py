class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        res = 1
        nums = [(i - k, i + k) for i in nums]
        numOperationsK = numOperations
        for i in range(len(nums)):
            j = i + 1
            intersection = nums[i]
            while j < len(nums):
                if numOperations == 0:
                    return res
                intersection = self.intersectionPair(
                    intersection[0], intersection[1], nums[j][0], nums[j][1]
                )
                if not intersection:
                    break
                res = max(res, j - i + 1)
                j += 1
                numOperations -= 1
        return numOperationsK

    def intersectionPair(self, x1, y1, x2, y2):
        start = max(x1, x2)
        end = min(y1, y2)
        if start <= end:
            return (start, end)
        else:
            return None


print(Solution().maxFrequency(nums=[5, 11, 20, 20], k=5, numOperations=1))
print(Solution().maxFrequency(nums=[1, 4, 5], k=1, numOperations=2))
print(Solution().maxFrequency([1, 2, 4, 99, 81], k=5, numOperations=2))  # 3
print(Solution().maxFrequency([1, 4, 8, 13], 5, 2))  # 2
print(Solution().maxFrequency([3, 9, 6], 2, 1))  # 1
print(Solution().maxFrequency([1, 90], 76, 1))  # 1
print(Solution().maxFrequency([2], 7, 0))
