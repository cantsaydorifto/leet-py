class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.res = ""
        self.dp = {}
        self.dfs(0, len(s) - 1)
        return self.res

    def dfs(self, i: int, j: int):
        if i > j:
            return
        if (i, j) in self.dp:
            return
        if self.isPalindrome(i, j):
            if j - i + 1 > len(self.res):
                self.res = self.s[i : j + 1]
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)

    def isPalindrome(self, i: int, j: int):
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        p, q = i, j
        while p < q:
            if self.s[p] != self.s[q]:
                self.dp[(i, j)] = False
                return self.dp[(i, j)]
            p += 1
            q -= 1
        self.dp[(i, j)] = True
        return self.dp[(i, j)]


print(Solution().longestPalindrome(s="babad"))
print(Solution().longestPalindrome(s="bb"))
print(Solution().longestPalindrome(s="abbcccbbbcaaccbababcbcabca"))
