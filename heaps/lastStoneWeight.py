import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        i = len(stones)
        while i > 1:
            el1, el2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if el1 != el2:
                heapq.heappush(stones, -abs(el1 - el2))
                i -= 1
            else:
                i -= 2
        return -heapq.heappop(stones) if stones else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(Solution().lastStoneWeight([1]))
print(Solution().lastStoneWeight([2, 2]))
