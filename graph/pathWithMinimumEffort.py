class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        q = [(0, 0, 0)]
        drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        import heapq

        while q:
            effort, i, j = heapq.heappop(q)
            if (i, j) in visited:
                continue
            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                return effort
            visited.add((i, j))
            for dr, dc in drs:
                if (
                    -1 < i + dr < len(heights)
                    and -1 < j + dc < len(heights[0])
                    and (i + dr, j + dc) not in visited
                ):
                    heapq.heappush(
                        q,
                        (
                            max(effort, abs(heights[i + dr][j + dc] - heights[i][j])),
                            i + dr,
                            j + dc,
                        ),
                    )
        return -1


print(Solution().minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(Solution().minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(
    Solution().minimumEffortPath(
        [[10, 8], [10, 8], [1, 2], [10, 3], [1, 3], [6, 3], [5, 2]]
    )
)
print(
    Solution().minimumEffortPath(
        heights=[
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
    )
)
