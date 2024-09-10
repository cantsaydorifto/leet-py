class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backtrack(res, nums, 0, [])
        return res

    def backtrack(
        self,
        res: list[int],
        nums: list[int],
        idx: int,
        curSubset: list[int],
        numSet: set = set(),
    ):
        if len(curSubset) == len(nums):
            res.append(curSubset.copy())
            return
        for i in range(len(nums)):
            if nums[i] in numSet:
                continue
            curSubset.append(nums[i])
            numSet.add(nums[i])
            self.backtrack(res, nums, i, curSubset)
            numSet.remove(nums[i])
            curSubset.pop()


print(Solution().permute(nums=[1, 2, 3]))
print(Solution().permute(nums=[0, 1]))
print(Solution().permute([1]))
