import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def keepKelements(self):
        i = len(self.nums)
        while i > self.k:
            heapq.heappop(self.nums)
            i -= 1

    def add(self, val: int) -> int:
        # print("VAL: ", val)
        # print(self.nums)
        heapq.heappush(self.nums, val)
        self.keepKelements()
        # print(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
kthEl = KthLargest(3, [4, 5, 8, 2])
print(kthEl.add(3))
print(kthEl.add(5))
print(kthEl.add(10))
print(kthEl.add(9))
print(kthEl.add(4))
