class Solution:
    def stringSequence(self, target: str) -> list[str]:
        res = []
        s = ""
        for ch in target:
            i = 0
            possibleChar = "a"
            while i < 26:
                possibleChar = chr(ord("a") + i)
                if possibleChar == ch:
                    s += possibleChar
                    res.append(s)
                    break
                res.append(s + possibleChar)
                i += 1
        return res

    def stringSequenceRepeat(self, target: str) -> list[str]:
        res = []
        cur = ""
        for ch in target:
            i = 0
            while i < 26:
                if chr(i + ord("a")) == ch:
                    cur += ch
                    break
                res.append(cur + chr(i + ord("a")))
                i += 1
            res.append(cur)
        return res


print(Solution().stringSequence("abc"))
print(Solution().stringSequence("he"))
