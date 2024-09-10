class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        self.backtrack(res, candidates, 0, [], 0, target)
        return res

    def backtrack(
        self,
        res: list[int],
        candidates: list[int],
        idx: int,
        curSubset: list[int],
        curSum: int,
        target: int,
    ):
        if curSum > target:
            return
        if curSum == target:
            res.append(curSubset.copy())
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            curSubset.append(candidates[i])
            curSum += candidates[i]
            self.backtrack(res, candidates, i + 1, curSubset, curSum, target)
            curSum -= candidates[i]
            curSubset.pop()


print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
