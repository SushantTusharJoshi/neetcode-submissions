from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:                 # CHANGE: fires = rotten (was land 1)
                    q.append((r, c))
                elif grid[r][c] == 1:               # CHANGE: grass = fresh (was water 0)
                    fresh += 1

        if fresh == 0:                              # CHANGE: no grass -> 0 minutes (was -1)
            return 0

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:   # CHANGE: fresh
                        grid[nr][nc] = 2            # CHANGE: it rots
                        fresh -= 1                  # CHANGE: one less grass
                        q.append((nr, nc))
            dist += 1

        return dist - 1 if fresh == 0 else -1       # CHANGE: rocks may block some