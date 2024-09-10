class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.backtrack(res, nums, [])
        return res

    def backtrack(
        self,
        res: list[int],
        nums: list[int],
        curSubset: list[int],
        numSet: set = set(),
    ):
        if len(curSubset) == len(nums):
            res.append(curSubset.copy())
            return
        for i in range(len(nums)):
            if ((i, nums[i]) in numSet) or (
                i > 0 and nums[i] == nums[i - 1] and (i - 1, nums[i - 1]) not in numSet
            ):
                continue
            curSubset.append(nums[i])
            numSet.add((i, nums[i]))
            self.backtrack(res, nums, curSubset, numSet)
            numSet.remove((i, nums[i]))
            curSubset.pop()


print(Solution().permuteUnique(nums=[1, 1, 2]))
# print(Solution().permuteUnique(nums=[1, 2, 3]))
# print(Solution().permuteUnique(nums=[0, 1]))
# print(Solution().permuteUnique([1]))
