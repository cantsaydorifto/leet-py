class Solution:
    def isBalanced(self, num: str) -> bool:
        sumEven, sumOdd = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                sumEven += int(num[i])
                continue
            sumOdd += int(num[i])
        return sumEven == sumOdd


print(Solution().isBalanced("1234"))
print(Solution().isBalanced("24123"))
