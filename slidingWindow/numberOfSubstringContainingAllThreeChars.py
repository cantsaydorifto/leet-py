class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, l, abcCount = 0, 0, [0, 0, 0]
        for i in s:
            abcCount[ord(i) - ord("a")] += 1
            while 0 not in abcCount:
                abcCount[ord(s[l]) - ord("a")] -= 1
                l += 1
            res += l
        return res


print(Solution().numberOfSubstrings(s="abcabc"))
