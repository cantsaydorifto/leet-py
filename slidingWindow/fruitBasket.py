class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        res, l, d = 0, 0, {}
        for i in range(len(fruits)):
            d[fruits[i]] = d.get(fruits[i], 0) + 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l += 1
            res = max(res, i - l + 1)
        return res


print(Solution().totalFruit(fruits=[0]))
print(Solution().totalFruit(fruits=[1, 2, 1]))
print(Solution().totalFruit(fruits=[0, 1, 2, 2]))
print(Solution().totalFruit(fruits=[1, 2, 3, 2, 2]))
