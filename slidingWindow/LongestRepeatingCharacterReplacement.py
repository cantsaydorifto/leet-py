class Solution:
    def characterReplacementOptimized(self, s: str, k: int) -> int:
        res, l, d, maxInMap = 0, 0, {}, 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            maxInMap = max(maxInMap, d[s[r]])
            while r - l + 1 - maxInMap > k:
                d[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        res, l, d = 0, 0, {}
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            while r - l + 1 - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res


print(Solution().characterReplacement(s="ABAB", k=2))
print(Solution().characterReplacement(s="AABABBA", k=1))
