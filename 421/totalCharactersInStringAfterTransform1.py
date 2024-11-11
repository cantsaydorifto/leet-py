class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res = 0
        self.memo = {}
        for i in s:
            res += self.dfs(i, t)
        return res % (10**9 + 7)

    def dfs(self, s: str, t: int):
        if t + (ord(s) - ord("a")) < 26:
            return 1
        if (s, t) in self.memo:
            return self.memo[(s, t)]
        newT = t - (ord("z") - ord(s) + 1)
        self.memo[(s, t)] = (self.dfs("a", newT) + self.dfs("b", newT)) % (10**9 + 7)
        return self.memo[(s, t)]

    def lengthAfterTransformationsBrute(self, s: str, t: int) -> int:
        for _ in range(t):
            res = ""
            for i in s:
                if i == "z":
                    res += "ab"
                    continue
                res += chr(ord(i) + 1)
            s = res
        return len(res) % (10**9 + 7)


# print(Solution().dfs(s="y", t=50))
# print(Solution().lengthAfterTransformations(s="azbk", t=1))
print(Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517))
print(Solution().lengthAfterTransformations("y", 27))
print(Solution().lengthAfterTransformations("cu", 5))
