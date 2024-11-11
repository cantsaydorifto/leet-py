import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        q = [(0, 0, 0, 2)]
        drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        adjTimeSwitch = {1: 2, 2: 1}
        while q:
            time, i, j, prevAdjTime = heapq.heappop(q)
            if (i, j) in visited:
                continue
            if i == len(moveTime) - 1 and j == len(moveTime[0]) - 1:
                return time
            visited.add((i, j))
            for dr, dc in drs:
                if (
                    -1 < i + dr < len(moveTime)
                    and -1 < j + dc < len(moveTime[0])
                    and (i + dr, j + dc) not in visited
                ):
                    timeToNextRoom = (
                        max(moveTime[i + dr][j + dc] - time, 0)
                        + adjTimeSwitch[prevAdjTime]
                    )
                    heapq.heappush(
                        q,
                        (
                            time + timeToNextRoom,
                            i + dr,
                            j + dc,
                            adjTimeSwitch[prevAdjTime],
                        ),
                    )
        return -1


print(Solution().minTimeToReach(moveTime=[[0, 4], [4, 4]]))
print(Solution().minTimeToReach(moveTime=[[0, 0, 0, 0], [0, 0, 0, 0]]))
print(Solution().minTimeToReach(moveTime=[[0, 1], [1, 2]]))
