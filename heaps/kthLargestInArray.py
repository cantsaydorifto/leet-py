import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        return -heapq.heappop(nums)


print(Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
