class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while 1:
            if self.digitProduct(i) % t == 0:
                return i
            i += 1

    def digitProduct(self, i: int):
        res = 1
        while i > 0:
            res *= i % 10
            i //= 10
        return res


print(Solution().smallestNumber(10, 2))
print(Solution().smallestNumber(15, 3))
# print(Solution().digitProduct(16))
