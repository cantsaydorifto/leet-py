class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split()
        for i in range(len(arr)):
            if arr[i - 1][-1] != arr[i][0]:
                return False
        return True

    def isCircularSentence2(self, sentence: str) -> bool:
        arr = sentence.split()
        for i in range(len(arr)):
            if i in [len(arr) - 1, 0] and arr[-1][-1] != arr[0][0]:
                return False
            if ((i + 1) < len(arr)) and arr[i][-1] != arr[i + 1][0]:
                return False
        return True


# print(Solution().isCircularSentence(sentence="leetcode exercises sound delightful"))
print(Solution().isCircularSentence(sentence="eetcode"))
# print(Solution().isCircularSentence(sentence="Leetcode is cool"))
