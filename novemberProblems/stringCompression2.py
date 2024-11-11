class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.memo, self.s = {}, s
        return self.dfs(0, k, 0, "")

    def dfs(self, i: int, k: int, prevCnt: int, prevCh: str):
        cacheKeyToCheck = (i, k, prevCnt, prevCh)
        if k < 0:
            return float("inf")
        if i == len(self.s):
            return 0
        if cacheKeyToCheck in self.memo:
            return self.memo[cacheKeyToCheck]
        if self.s[i] == prevCh:
            self.memo[cacheKeyToCheck] = int(prevCnt in [1, 9, 99]) + self.dfs(
                i + 1, k, prevCnt + 1, self.s[i]
            )
            return self.memo[cacheKeyToCheck]
        self.memo[cacheKeyToCheck] = min(
            self.dfs(i + 1, k - 1, prevCnt, prevCh),
            1 + self.dfs(i + 1, k, 1, self.s[i]),
        )
        return self.memo[cacheKeyToCheck]


print(Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2))
print(Solution().getLengthOfOptimalCompression(s="aabbaa", k=2))
print(Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0))
print(Solution().getLengthOfOptimalCompression(s="llllllllllttttttttt", k=1))
