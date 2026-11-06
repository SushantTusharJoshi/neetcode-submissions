from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0]) 
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(starts):
            q = deque()
            visited = set()
            for r,c in starts:
                q.append((r,c))
                visited.add((r,c))
            
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r +dr, c + dc
                    if ( 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        q.append((nr,nc))
                        visited.add((nr,nc))
            
            return visited

        pac_starts = [(0,c) for c in range(COLS)] + [(r,0) for r in range(ROWS)]
        atl_starts = [(ROWS - 1,c) for c in range(COLS)] + [(r,COLS - 1) for r in range(ROWS)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        return [list(cell) for cell in pac & atl]




