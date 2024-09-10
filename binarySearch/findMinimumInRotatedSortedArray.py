class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            mid = (l + r) // 2
            res = min(nums[mid], res)
            if nums[l] == nums[mid]:  # for duplicates
                l += 1
            # or
            # if nums[r] == nums[mid]: #Same Thing
            #     r -= 1
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res


print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
print(Solution().findMin(nums=[2, 1, 2, 2, 2]))
print(Solution().findMin(nums=[10, 1, 10, 10, 10]))
print(Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin(nums=[0, 0, 1, 2, 4, 5, 6, 7, 0, 0]))
print(Solution().findMin(nums=[11, 13, 15, 17]))
