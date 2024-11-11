class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]):
        return self.dfs(s, t, nums)

    def dfs(self, s: str, t: int, nums: list[int]):
        if t == 0:
            return s
        curStr = ""
        if len(s) == 1:
            k = nums[ord(s) - ord("a")]
            for i in range(1, k + 1):
                ch = chr(((ord(s) - ord("a") + i) % 26) + ord("a"))
                curStr += ch
        else:
            for i in s:
                curStr += self.dfs(i, t, nums)
        return self.dfs(curStr, t - 1, nums)


print(
    Solution().lengthAfterTransformations(
        s="abcyy",
        t=2,
        nums=[
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
        ],
    )
)

print(
    Solution().lengthAfterTransformations(
        s="azbk",
        t=1,
        nums=[
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
        ],
    )
)
