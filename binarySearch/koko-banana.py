import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        self.piles = piles
        self.h = h
        self.res = max(self.piles)
        self.binarySearch()
        return self.res

    def isPossible(self, k: int):
        hrsRequired = 0
        for i in self.piles:
            hrsRequired += math.ceil(i / k)
        return hrsRequired <= self.h

    def binarySearch(self):
        l, r = 1, max(self.piles)
        while l <= r:
            mid = (l + r) // 2
            if self.isPossible(mid):
                self.res = min(self.res, mid)
                r = mid - 1
            else:
                l = mid + 1


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
