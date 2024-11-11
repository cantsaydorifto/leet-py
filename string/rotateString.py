class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return (s + s).find(goal) != -1 and len(s) == len(goal)
