class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        res = []
        i = 0
        while i < len(original):
            res.append(original[i : i + n])
            i += n
        return res
        # return [original[i * n: (i + 1) * n] for i in range(m)]


print(Solution().construct2DArray([1, 2, 3, 4], 2, 2))
