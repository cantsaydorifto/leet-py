class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res, s1Count, s2CurCount = False, [0] * 26, [0] * 26
        l, r = 0, len(s1) - 1
        if len(s2) < len(s1):
            return False
        for i in s1:
            s1Count[ord(i) - ord("a")] += 1
        for i in range(r + 1):
            s2CurCount[ord(s2[i]) - ord("a")] += 1
        while r < len(s2):
            if s1Count == s2CurCount:
                res = True
                break
            s2CurCount[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
            if r == len(s2):
                break
            s2CurCount[ord(s2[r]) - ord("a")] += 1
        return res


print(Solution().checkInclusion(s1="ab", s2="a"))
print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
