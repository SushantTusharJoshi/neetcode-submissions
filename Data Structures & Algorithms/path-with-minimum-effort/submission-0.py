import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])      # ← added
        heap = [(0, 0, 0)]                              # (effort, r, c)
        visited = set()
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]

        while heap:
            e, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            if r == rows - 1 and c == cols - 1:
                return e                                # ← added

            visited.add((r, c))                         # ← added

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    d = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush (heap, (max(e, d), nr, nc))