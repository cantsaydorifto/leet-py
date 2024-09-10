class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.backtrack(res, nums, 0, [])
        return res

    def backtrack(
        self,
        res: list[int],
        nums: list[int],
        idx: int,
        curSubset: list[int],
    ):
        res.append(curSubset.copy())
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            curSubset.append(nums[i])
            self.backtrack(res, nums, i + 1, curSubset)
            curSubset.pop()


print(Solution().subsetsWithDup([1, 2, 2]))
print(Solution().subsetsWithDup([0]))
