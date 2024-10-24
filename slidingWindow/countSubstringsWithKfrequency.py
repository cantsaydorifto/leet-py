class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res, l, d = 0, 0, {}
        for i in s:
            d[i] = d.get(i, 0) + 1
            while d[i] == k:
                d[s[l]] -= 1
                l += 1
            res += l
        return res

    def numberOfSubstringsN2(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = [0] * 26
            for j in range(i, len(s)):
                count[ord(s[j]) - ord("a")] += 1
                if count[ord(s[j]) - ord("a")] == k:
                    res += len(s) - 1 - j + 1
                    break
        return res

    def calculateForKsizeWindow(self, s: str, windowSize: int, k: int):
        count = {}
        for i in range(windowSize):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] += 1
        l, r = 0, windowSize - 1
        while r < len(s):
            # print(count, l, r)
            for val in count.values():
                if val >= k:
                    self.res += 1
                    # self.res.append(s[l : r + 1])
                    break
            count[s[l]] -= 1
            r += 1
            l += 1
            if r == len(s):
                break
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
        return self.res

    def numberOfSubstringsComplicatedOne(self, s: str, k: int) -> int:
        # self.res = []
        self.res = 0
        for i in range(k, len(s) + 1):
            self.calculateForKsizeWindow(s, i, k)
        return self.res


print(Solution().numberOfSubstrings("aba", 2))
print(Solution().numberOfSubstrings("abacb", 2))
# print(Solution().numberOfSubstrings("abcde", 1))
# print(Solution().calculateForKsizeWindow("abacb", 5, 2))
# print(Solution().calculateForKsizeWindow("abcde", 1))
