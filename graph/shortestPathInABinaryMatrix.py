class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        visited = set((0, 0))
        from collections import deque

        if grid[0][0] != 0:
            return -1
        q = deque([(0, 0, 1)])
        drs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        while q:
            r, c, d = q.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return d
            for dr, dc in drs:
                if (
                    -1 < r + dr < len(grid)
                    and -1 < c + dc < len(grid[0])
                    and grid[r + dr][c + dc] != 1
                    and (r + dr, c + dc) not in visited
                ):
                    q.append((r + dr, c + dc, d + 1))
                    visited.add((r + dr, c + dc))
        return -1


print(Solution().shortestPathBinaryMatrix([[0]]))
print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]))
print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]))
