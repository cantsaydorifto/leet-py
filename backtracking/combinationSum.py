class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        self.backtack(res, candidates, 0, [], 0, target)
        return res

    def backtack(
        self,
        res: list[int],
        candidates: list[int],
        idx: int,
        curSubset: list[int],
        curSum: int,
        target: int,
    ):
        if target < curSum:
            return
        if target == curSum:
            res.append(curSubset.copy())
        for i in range(idx, len(candidates)):
            curSubset.append(candidates[i])
            curSum += candidates[i]
            self.backtack(res, candidates, i, curSubset, curSum, target)
            curSubset.pop()
            curSum -= candidates[i]


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
print(Solution().combinationSum(candidates=[2, 3, 5], target=8))
print(Solution().combinationSum(candidates=[2], target=1))
