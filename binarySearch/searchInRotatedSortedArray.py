class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:  # for duplicates
                l += 1
            # or
            # if nums[r] == nums[mid]: #Same Thing
            #     r -= 1
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(Solution().search(nums=[1], target=0))
print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
print(Solution().search(nums=[2, 5, 6, 0, 0, 0, 0], target=350))
print(Solution().search(nums=[1, 0, 1, 1, 1], target=0))
