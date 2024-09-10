class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = float("inf")
        while l <= r:
            mid = (l + r) // 2
            if self.isCapacityValid(weights, mid, days):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

    def isCapacityValid(self, weights: list[int], k: int, days: int):
        i = 0
        daysRequired = 0
        while i < len(weights):
            totalWeight = 0
            while i < len(weights) and totalWeight + weights[i] <= k:
                totalWeight += weights[i]
                i += 1
            daysRequired += 1
        return daysRequired <= days


print(Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(Solution().shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
print(Solution().shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
