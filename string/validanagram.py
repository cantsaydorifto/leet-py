class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagramWithUnicodeChars(s, t)

    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0] * 26
        for i in s:
            cnt[ord(i) - ord("a")] += 1
        for i in t:
            cnt[ord(i) - ord("a")] -= 1
        return cnt == [0] * 26

    def isAnagramWithUnicodeChars(self, s: str, t: str) -> bool:
        cnt = {}
        for i in s:
            cnt[i] = cnt.get(i, 0) + 1
        for t in s:
            if t not in cnt:
                return False
            cnt[i] -= 1
        for val in cnt.values():
            if val != 0:
                return False
        return True
