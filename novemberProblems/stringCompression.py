class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            s += chars[i] + ("" if j - i == 1 else str(j - i))
            i = j
        for i in range(len(chars)):
            if i >= len(s):
                break
            chars[i] = s[i]
        return len(s)


print(Solution().compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(Solution().compress(chars=["a", "a"]))
print(
    Solution().compress(
        chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    )
)
