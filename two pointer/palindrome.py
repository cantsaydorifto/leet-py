class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() if i.isalnum() else "" for i in s])
        print(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
