class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, t in times:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, t))
        visited = set()
        import heapq

        q = [(0, k)]
        res = -1
        while q:
            time, fromNode = heapq.heappop(q)
            if fromNode in visited:
                continue
            res = max(res, time)
            visited.add(fromNode)
            for i, j in graph[fromNode]:
                if i in visited:
                    continue
                heapq.heappush(q, (time + j, i))
        return res if len(visited) == n else -1


print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
print(Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1))
