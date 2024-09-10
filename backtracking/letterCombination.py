class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.res = []
        self.digits = digits
        self.letterMapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.backtrack(0, "")
        print(self.res)
        return self.res

    def backtrack(
        self,
        i: int,
        combinationStr: str,
    ):
        if len(combinationStr) == len(self.digits):
            if combinationStr != "":
                self.res.append(combinationStr)
            return
        for s in self.letterMapping[self.digits[i]]:
            self.backtrack(i + 1, combinationStr + s)


Solution().letterCombinations("23")
Solution().letterCombinations("")
