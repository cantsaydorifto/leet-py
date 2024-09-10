class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        validOperators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in validOperators:
                st.append(i)
                continue
            if i == "+":
                val1, val2 = int(st.pop()), int(st.pop())
                st.append(val1 + val2)
            if i == "*":
                val1, val2 = int(st.pop()), int(st.pop())
                st.append(val1 * val2)
            if i == "-":
                val1, val2 = int(st.pop()), int(st.pop())
                st.append(val2 - val1)
            if i == "/":
                val1, val2 = int(st.pop()), int(st.pop())
                st.append(val2 / val1)
        return int(st[0])


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["18"]))
