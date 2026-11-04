class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        count = 0
        for i in range(0,n):
            if i not in visited:
                count += 1
                dfs(i)
            
        return count
                