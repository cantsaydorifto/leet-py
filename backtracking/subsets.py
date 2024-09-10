class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backtrack2(res, nums, 0, [])
        return res

    def backtrack(
        self, res: list[int], nums: list[int], idx: int, curSubset: list[int]
    ):
        res.append(curSubset.copy())
        for j in range(idx, len(nums)):
            curSubset.append(nums[j])
            self.backtrack(res, nums, j + 1, curSubset)
            curSubset.pop()

    def backtrack2(
        self, res: list[int], nums: list[int], idx: int, curSubset: list[int]
    ):
        if idx >= len(nums):
            res.append(curSubset)
            return
        self.backtrack2(res, nums, idx + 1, curSubset + [nums[idx]])
        self.backtrack2(res, nums, idx + 1, curSubset)


print(Solution().subsets([1, 2, 3]))
