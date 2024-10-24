class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l, charSet = 0, 0, set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r - l + 1, res)
        return res

    def lengthOfLongestSubstringPrev(self, s: str) -> int:
        chars = set()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] in chars:
                chars.remove(s[l])
                l += 1
                continue
            chars.add(s[r])
            r += 1
            res = max(res, r - l)
        return res


print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
print(Solution().lengthOfLongestSubstring(s="bbbbb"))
print(Solution().lengthOfLongestSubstring(s="pwwkew"))
