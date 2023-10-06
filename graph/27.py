from collections import defaultdict

class Solution:
    def topoSort(self, node, adj, vis, st):
        vis[node] = 1
        for v, _ in adj[node]:
            if not vis[v]:
                self.topoSort(v, adj, vis, st)
        st.append(node)

    def shortestPath(self, N, M, edges):
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
        
        vis = [0] * N
        st = []

        for i in range(N):
            if not vis[i]:
                self.topoSort(i, adj, vis, st)
        
        dist = [float('inf')] * N
        dist[0] = 0

        while st:
            node = st.pop()
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = wt + dist[node]

        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist

N = 6
M = 7
edges = [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]
obj = Solution()
ans = obj.shortestPath(N, M, edges)

for i in range(len(ans)):
    print(ans[i], end=" ")
