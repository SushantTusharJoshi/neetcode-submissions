class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        heap = [(0,k)]
        visited = set()

        for u,v,t in times:
            adj[u].append((v,t))

        while heap:
            time,node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            res = time
            for nei,w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,(time + w,nei))
            
        return res if len(visited) == n else -1