class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = {}
        for s in strs:
            chars = [0] * 26
            for ch in s:
                chars[ord(ch) - ord("a")] += 1
            charTuple = tuple(chars)
            if charTuple not in mp:
                mp[charTuple] = []
            mp[charTuple].append(s)
        return list(mp.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
