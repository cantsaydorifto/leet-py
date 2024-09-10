class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        for ch in s:
            chars[ord(ch) - ord("a")] += 1
        for ch in t:
            chars[ord(ch) - ord("a")] -= 1
        return chars == [0] * 26

    def isAnagramWithUnicodeChars(self, s: str, t: str) -> bool:
        chars = {}
        for ch in s:
            if not ch in chars:
                chars[ch] = 0
            chars[ch] += 1
        for ch in t:
            if not ch in chars:
                return False
            chars[ch] -= 1
        for v in chars.values():
            if v != 0:
                return False
        return True
