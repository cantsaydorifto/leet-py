class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dict = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in dict:
                st.append(i)
                continue
            if st and dict[i] == st[-1]:
                st.pop()
            else:
                return False
        return len(st) == 0


print(Solution().isValid("()[]{}"))
