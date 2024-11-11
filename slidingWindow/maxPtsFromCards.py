class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        res = float("-inf")
        r = len(cardPoints) - 1
        l = r - k + 1
        curSum = 0
        for i in range(l, r + 1):
            curSum += cardPoints[i]
        for i in range(k + 1):
            res = max(curSum, res)
            curSum -= cardPoints[l % len(cardPoints)]
            l += 1
            r += 1
            curSum += cardPoints[r % len(cardPoints)]
        return res


print(Solution().maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(Solution().maxScore(cardPoints=[2, 2, 2], k=2))
print(Solution().maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))
