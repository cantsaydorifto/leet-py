class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        leftMostIdx = self.binarySearch(nums, target, True)
        rightMostIdx = self.binarySearch(nums, target, False)
        return [leftMostIdx, rightMostIdx]

    def binarySearch(self, nums: list[int], target: int, leftMost: bool) -> int:
        l, r, idx = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                idx = mid
                if leftMost:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return idx


print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(Solution().searchRange(nums=[], target=0))
