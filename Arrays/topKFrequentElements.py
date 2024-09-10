class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        res = []
        frequency = [[] for i in range((len(nums) + 1))]
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        for key, val in counter.items():
            frequency[val].append(key)
        print(frequency)
        for i in range(len(frequency) - 1, -1, -1):
            for el in frequency[i]:
                res.append(el)
                if len(res) == k:
                    return res
        return res


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
