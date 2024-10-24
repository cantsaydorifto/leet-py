class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s1, s2 = p, s
        res, s1Count, s2CurCount = [], [0] * 26, [0] * 26
        l, r = 0, len(s1) - 1
        if len(s2) < len(s1):
            return []
        for i in s1:
            s1Count[ord(i) - ord("a")] += 1
        for i in range(r + 1):
            s2CurCount[ord(s2[i]) - ord("a")] += 1
        while r < len(s2):
            if s1Count == s2CurCount:
                res.append(l)
            s2CurCount[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
            if r == len(s2):
                break
            s2CurCount[ord(s2[r]) - ord("a")] += 1
        return res


print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
print(Solution().findAnagrams(s="abab", p="ab"))
