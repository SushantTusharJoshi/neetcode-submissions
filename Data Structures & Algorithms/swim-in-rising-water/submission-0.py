import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r,c) in visited:
                continue

            if r == n - 1 and c == n - 1:
                return t
            
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))