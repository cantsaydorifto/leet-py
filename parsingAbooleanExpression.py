class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for i in range(len(expression) - 1, -1, -1):
            if expression[i] in [",", "!", "|", "&"]:
                continue
            if expression[i] != "(":
                if expression[i] in ["t", "f"]:
                    st.append(True if expression[i] == "t" else False)
                else:
                    st.append(expression[i])
                continue
            operation = expression[i - 1]
            ch = st.pop()
            if ch in ["t", "f"]:
                ch = True if ch == "t" else False
            res = ch
            if operation == "!":
                res = not ch
            while ch != ")":
                ch = st.pop()
                if ch == ")":
                    break
                if operation == "|":
                    res = res or ch
                elif operation == "&":
                    res = res and ch
            st.append(res)
        return st[0]


print(Solution().parseBoolExpr(expression="&(|(f,t,f,t))"))
print(Solution().parseBoolExpr(expression="|(f,f,f,t)"))
print(Solution().parseBoolExpr(expression="!(&(f,t))"))
