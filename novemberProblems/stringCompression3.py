class Solution:
    def compressedString(self, word: str) -> str:
        l = 1
        comp = ""
        i = 0
        for i in range(1, len(word)):
            if l == 9:
                comp += "9" + word[i - 1]
                l = 1
                continue
            if word[i - 1] == word[i]:
                l += 1
                continue
            comp += str(l) + word[i - 1]
            l = 1
        comp += str(l) + word[i]
        return comp


print(Solution().compressedString("aaaaaaaaaaaaaabb"))
print(Solution().compressedString("abcde"))
print(Solution().compressedString("d"))
